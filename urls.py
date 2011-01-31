from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
   (r'^events/', include('events.urls')),
   (r'^admin/', include(admin.site.urls)),
)
