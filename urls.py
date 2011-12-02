from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^maps/$', 'maps.views.search', name='maps'),
#    url(r'^flats/$', TemplateView.as_view(template_name="flats.html"), name='flats'),
    url(r'^flats/$', 'flats.views.show_chart', name='flats'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    # url(r'^s1idernet/', include('s1idernet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()