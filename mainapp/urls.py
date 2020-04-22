from django.conf.urls import  include, url
from django.contrib import admin

from mainapp import views
from django.conf.urls.static import static

from django.conf import settings



urlpatterns = [
    url(r'^login$', views.login, ),
    url(r'^checkreg$', views.checkregister, ),
    url(r'^postcomplain$', views.postcomplain, ),
    url(r'^interested$', views.interested, ),
    url(r'^feedandclubs$', views.feedandclubs, ),
    url(r'^importantcontacts$', views.importantcontacts, ),
    url(r'^timetable$', views.timetable, ),
    url(r'^notification$', views.notification, ),
    url(r'^pors$', views.pors, ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


