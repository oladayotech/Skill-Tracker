from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets
from .models import DailyLog
from .serializers import DailyLogSerializer

from .models import Journal
from .quote_generator import Quote_Selector

import random
from datetime import date

# Create your views here.
def home(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    return render(request, 'index.html')

def navbar(request):
    # Check if the user is already authenticated
    # if request.user.is_authenticated:
    #     return redirect('dashboard')  # Redirect to the dashboard if already logged in
    return render(request, 'navbar.html')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        # if email:
        #     error_message = 'Account exist! Login'
        #     return render(request, 'signup.html', {'error_message_email':error_message})
        if password == password1:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('onboarding')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
    return render(request, 'signup.html')

def user_login(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {"error_message":error_message})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def skills(request):
    return render(request, 'skills.html')

@login_required
def onboarding(request):
    return render(request, 'onboarding.html')

@login_required
def role_selection(request):
    return render(request, 'role_selection.html')

@login_required
def learning_goals(request):
    return render(request, 'learning_goals.html')

@login_required
def dashboard(request):
    today = date.today()
    journal_count = Journal.objects.filter(created_at__date=today).count()
    # coding_hours = request.user.profile.get_today_hours()

    ranges = random.randint(0,8)
    quote = Quote_Selector(ranges)
    return render(request, 'dashboard.html', {'quote':quote, 'journal_count':journal_count})

@login_required
def dashboard_data(request):
    today = date.today()

    journal_count = Journal.objects.filter(created_at__date=today).count()
    # coding_hours = request.user.profile.get_today_hours()  # Replace with actual logic

    return JsonResponse({
        'journal_count': journal_count,
        # 'coding_hours': coding_hours,
    })
    
def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

# def journal(request):
#     if request.method == "POST":
#         journal_content = request.POST['journal_content']
#         journal_image = request.POST['journal_image']
#         new_journal = Journal.objects.create(
#             user = request.user,
#             journal_content = journal_content,
#             journal_image = journal_image,
#         )
#         new_journal.save()
#     journal_list = Journal.objects.filter(user = request.user)
#     return render(request, 'journal.html', {'journal_list':journal_list})

def journal(request):
    if request.method == "POST":
        journal_content = request.POST.get('journal_content')
        journal_image = request.FILES.get('journal_image')  # Use FILES for uploaded media

        new_journal = Journal.objects.create(
            user=request.user,
            journal_content=journal_content,
            journal_image=journal_image
        )
        new_journal.save()

    journal_list = Journal.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal.html', {'journal_list': journal_list})

def journal_details(request, pk):
    journal_detail = Journal.objects.get(id=pk)
    if request.user == journal_detail.user:
        return render(request, 'journal_details.html', {'journal_detail':journal_detail})
    else:
        return redirect('journal')
    
class DailyLogViewSet(viewsets.ModelViewSet):
    queryset = DailyLog.objects.all()
    serializer_class = DailyLogSerializer