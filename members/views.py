from django.http import HttpResponse
from django.template import loader

from .models import Member


def members(request):
    my_members = Member.objects.all().values()
    my_members_name = Member._meta.verbose_name
    template = loader.get_template("all_members.html")
    context = {"my_members": my_members, "page_header": my_members_name.capitalize()}
    return HttpResponse(template.render(context, request))


def details(request, pk):
    my_members = Member.objects.get(id=pk)
    template = loader.get_template('details.html')
    context = {"my_members": my_members}
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
