from django.conf.urls.defaults import *
from startthedark.events import views

urlpatterns = patterns('',
                           
    url(r'^tonight/$',
        views.tonight,
        name='ev_tonight'),
    
    url(r'^create/$',
        views.create,
        name='ev_create'),
    
    url(r'^archive/$',
        views.archive,
        name='ev_archive'),
    
    url(r'^toggle-attendance/$',
        views.toggle_attendance,
        name='ev_toggle_attendance'),
    
    
    
)
