from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path('',views.index,name='index'),
    path('location_table', views.location_table, name='location_table'),
    # path('nextpage',views.nextpage,name='nextpage'),
    path('members', views.members, name='members'),
    path('excelinput', views.excelinput, name='excelinput')
    


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)