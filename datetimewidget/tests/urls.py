__author__ = 'asagli'

from django.conf import  settings
from django.views.generic import RedirectView
from django.views import static

try:
    # Removed in Django 1.6
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url
    
try:
    # Relocated in Django 1.6
    from django.conf.urls.defaults import pattern
except ImportError:
    # Completely removed in Django 1.10
    try:    
        from django.conf.urls import patterns
    except ImportError:
        patterns = None

from datetimewidget.tests import views 

_patterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
    url("^model_form_v3/$", views.dateTimeViewBootstrap3),
    url("^model_form_v2/$", views.dateTimeViewBootstrap2),
    url(r'^.*$', RedirectView.as_view(url='/model_form_v3/')),
]

if patterns is None:
    urlpatterns = _patterns
else:
    urlpatterns = patterns('', *_patterns)
