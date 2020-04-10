from django.urls import path
from . import views
urlpatterns = [
    path('', views.inquirys, name="inquirys")
]
