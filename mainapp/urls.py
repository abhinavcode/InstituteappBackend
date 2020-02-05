from django.urls import  include, path
from django.contrib import admin

from main_app import views
from django.conf.urls.static import static

from django.conf import settings



urlpatterns = [
    path('login', views.login, ),
    path('checkreg', views.checkregister, ),
    path('postcomplain', views.postcomplain, ),
    path('interested', views.interested, ),
    path('feedandclubs', views.feedandclubs, ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
