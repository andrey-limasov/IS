from django.urls import path

from isprofile import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dbinfo/', views.dbinfo, name='dbinfo'),
    path('docs/', views.docs, name='docs'),
    path('docs/<filename>/', views.docs, name='docs'),
]