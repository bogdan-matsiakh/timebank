from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from main import views

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', 'main.views.index_db'),
    #url(r'^$', 'main.views.index'),
    
    url(r'^channel$', 'main.views.channel'),
    #url(r'^fb$', 'main.views.fb'),
    #url(r'^fb/fb-auth$', 'main.views.fb'),
  #  url(r'^fb/', include('fb.urls')),
    # url(r'^timebank/', include('timebank.foo.urls')),
  #  url(r'^facebook/', include('django_facebook.urls')),
  #  url(r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
