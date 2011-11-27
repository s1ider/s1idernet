from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^maps/$', TemplateView.as_view(template_name="maps.html"), name='maps'),
    url(r'^maps/search/$', 'maps.views.search'),
    url(r'^flats/$', TemplateView.as_view(template_name="flats.html"), name='flats'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    # url(r'^s1idernet/', include('s1idernet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()