from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('StudentHelp/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def word(request, palabra):
    return HttpResponse("The word is %s." % palabra)