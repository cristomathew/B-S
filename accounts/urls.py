from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('register/confirm', views.confirmregister, name="confirmregister"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/myinquiries', views.myinquiries, name="myinquiries"),
    path('dashboard/inquiry', views.inquiry1, name="inquiry1"),
    path('dashboard/send_reply', views.send_reply, name="send_reply"),



]
