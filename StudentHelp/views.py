from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import RequestContext, loader


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
        'data': html
    })
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return HttpResponse(template.render(c))


def search_form(request):
    template = loader.get_template('StudentHelp/search.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def quiz(request):
    template = loader.get_template('StudentHelp/questionnaire.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def search2(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def search(request):
    template = loader.get_template('StudentHelp/results.html')
    q = request.GET['q']
    context = RequestContext(request, {
        'searched': q
    })
    return HttpResponse(template.render(context))