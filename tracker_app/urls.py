from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('navbar', views.navbar, name='navbar'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('skills/', views.skills, name='skills'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/data/', views.dashboard_data, name='dashboard-data'),
    path('about/', views.about, name='about'),
    path('journal/', views.journal, name='journal'),
    path('journal/journal-details/<int:pk>/', views.journal_details, name='journal-details'),
]