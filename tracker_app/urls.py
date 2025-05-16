from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('skills/', views.skills, name='skills'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/role-selection/', views.role_selection, name='role-selection'),
    path('onboarding/role-selection/stacks', views.stacks, name='stacks'),
    path('onboarding/role-selection/learning-goals', views.learning_goals, name='learning-goals'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/data/', views.dashboard_data, name='dashboard-data'),
    path('about/', views.about, name='about'),
    path('/<str:username>/', views.profile, name='profile'),
    path('journal/', views.journal, name='journal'),
    path('journal/journal-details/<int:pk>/', views.journal_details, name='journal-details'),
    # path('stacks/', views.profile, name='stacks'),
]