from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.contrib import messages

from rest_framework import viewsets
from .models import DailyLog
from .serializers import DailyLogSerializer
from .models import Journal, Profile, UserSelection
from .quote_generator import Quote_Selector

import random
import json
from datetime import date

# Create your views here.
def home(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    return render(request, 'index.html')

# def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            try:
                if User.objects.filter(username=username).exists():
                    error_message = 'Username taken!'
                    messages.error(request, "Username taken!")
                    return render(request, 'signup.html', {'error_message': 'Username already taken!'})
                    messages.error(request, "Username taken!")
                    return redirect('login')
                if User.objects.filter(email=email).exists():
                    error_message = 'Email taken!'
                    return render(request, 'signup.html', {'error_message': 'Email already taken!'})
                    return redirect('login')
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.success(request, "Account created successfully! Please log in.")
                login(request, user)
                return redirect('onboarding')
            except Exception as e:
                error_message = e
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
    return render(request, 'signup.html')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Already logged in

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password != password1:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already taken'})

        if User.objects.filter(email=email).exists(): # Handles error if email is taken
            return render(request, 'signup.html', {'error_message': 'Email already taken'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Optional: manually create profile only if not using signals
            # if not hasattr(user, 'profile'):
            #     Profile.objects.create(user=user)

            messages.success(request, "Account created successfully! Please log in.")
            login(request, user)  # Log them in immediately
            return redirect('onboarding')

        except Exception as e:
            return render(request, 'signup.html', {'error_message': str(e)})
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
    goals = [
        ("Start my career", "🚀"),
        ("Change my career", "🔀"),
        ("Grow in my current role", "📈"),
        ("Explore topics outside of work", "🔭"),
    ]
    return render(request, 'onboarding.html', {'goals':goals})

# def save_goal(request):
    if request.method == 'POST':
        try:
            data = json.load(request.body)
            goal = data.get('goal')
            if goal and request.user.is_authenticated:
                # update or create the UserGoal
                obj, created = UserGoal.objects.update_or_create(
                    user = request.user,
                    defaults={'goal':goal}
                )
                return JsonResponse({'status':'success'})
            else:
                return JsonResponse({'status':'unauthorized'}, status=401)
        except Exception as e:
            return JsonResponse({'status':'error', 'message':str(e)}, status = 500)
    return JsonResponse({'status': 'invalid method'}, status=405)


@csrf_exempt  # For AJAX fetch. Can replace with @csrf_protect if you're 100% sure CSRF is working
@login_required
def save_goal(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        goal = data.get('goal')

        try:
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.goal = goal
            profile.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

# def role_selection(request):
    if request.method == "POST":
        data = json.loads(request.POST.get('selectedItems', '[]'))
        # Save to DB for the current user
        UserSelection.objects.create(user=request.user, selection_type="role", data=data)
        return redirect('stacks')  # or whatever your next page URL name is

    return render(request, 'role_selection.html')

@login_required
def role_selection(request):
    return render(request, 'role_selection.html')

def save_role(request):
    if request.method == 'POST':
        role = request.POST.get('selected_role')
        profile,created = Profile.objects.get_or_create(user=request.user)
        profile.role = role
        profile.save()
        return redirect('stacks')  # Next page after selecting role
    return redirect('onboarding')

@login_required
def stacks(request):
    if request.method == "POST":
        data = json.loads(request.POST.get('selectedItems', '[]'))
        UserSelection.objects.create(user=request.user, selection_type="stack", data=data)
        return redirect('learning-goals')
    return render(request, 'stacks.html')

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

@login_required   
def profile(request, username):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

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