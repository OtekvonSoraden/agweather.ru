from django.urls import path
# from django.contrib import admin
# from website.views import signup

from . import views

app_name = "website"
urlpatterns = [
    path('', views.forecast, name='forecast'),
    path('forecast/', views.forecast, name="forecast"),
    path('archive/', views.archive, name="archive"),
    path('feedback/', views.feedback, name="feedback"),
    path('add_location/', views.LocationCreateView.as_view(),
         name="add_location"),
]
