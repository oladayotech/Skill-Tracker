from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('navbar', views.navbar, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('journal/', views.journal, name='journal'),
]