from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import RequestContext, loader
from StudentHelp.models import Poll, Choice


def index(request):
    template = loader.get_template('StudentHelp/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def word(request, palabra):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Welcome to the page %s" % request.path + ", \nthe word is %s." % palabra +
                        " and more information %s" % ua)


def display_meta(request):
    template = loader.get_template('StudentHelp/about.html')
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    c = RequestContext(request, {
        'data': '<table>%s</table>' % '\n'.join(html)
    })
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return HttpResponse(template.render(c))


def search_form(request):
    template = loader.get_template('StudentHelp/search.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def quiz(request):
    latest_poll_list = Poll.objects.order_by('id')[:5]
    template = loader.get_template('StudentHelp/questionnaire.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))


def search(request):
    template = loader.get_template('StudentHelp/results.html')
    if 'q' in request.GET:
        q = request.GET['q']
        context = RequestContext(request, {
            'searched': q
        })
    else:
        context = RequestContext(request, {
            'searched': 'Empty search form'
        })
    return HttpResponse(template.render(context))