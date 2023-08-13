from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    my_members = Member.objects.all().values()
    my_members_name = Member._meta.verbose_name
    template = loader.get_template("details.html")
    context = {"my_members": my_members}
    context["page_title"] = my_members_name.capitalize()
    print(context)

    return HttpResponse(template.render(context, request))
