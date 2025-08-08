from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.contrib import messages

from rest_framework import viewsets
# from .models import Goal
# from .serializers import DailyLogSerializer
from .models import Journal, Profile
from .quote_generator import Quote_Selector

import random
import json
from datetime import date

# Create your views here.
def home(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard if already logged in
    # return render(request, 'index.html')
    return render(request, 'index.html', {
        'solutions': [
            {'icon': 'bi-kanban-fill', 'title': 'Skill Dashboard', 'description': 'Monitor growth and milestones from a single place.'},
            {'icon': 'bi-journals', 'title': 'Mentor Matching', 'description': 'Get paired with mentors and stay accountable.'},
            {'icon': 'bi-calendar-check', 'title': 'Goal Planning', 'description': 'Set daily, weekly, and long-term goals to grow smarter.'},
        ],
        'steps': [
            {'icon': 'bi-person-plus', 'title': '1. Create an Account', 'description': 'Sign up and set your first goal.'},
            {'icon': 'bi-bar-chart-line', 'title': '2. Track Progress', 'description': 'Update skills and reflect on improvements.'},
            {'icon': 'bi-stars', 'title': '3. Celebrate Wins', 'description': 'Earn badges and stay motivated as you grow.'},
        ],
        'faqs': [
            {'question': 'Is SkillTracker free to use?', 'answer': 'Yes! You can get started with our free version and upgrade anytime.'},
            {'question': 'Can I invite friends or mentors?', 'answer': 'Absolutely. You can share progress and goals with your community.'},
        ]
    })

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
        
        # UserSelection.objects.filter(user=request.user).delete()
        # UserSelection.objects.update_or_create(user=request.user, selection_type="stack", data=data)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.stack = data
        profile.save()
        return redirect('learning-goals')
    return render(request, 'stacks.html')

@login_required
def learning_goals(request):
    return render(request, 'learning_goals.html')

@require_POST
@login_required
def submit_goals(request):
    try:
        data = json.loads(request.body)
        goals = data.get('goals', [])

        # Optional: Clear previous goals to avoid duplicates
        # Goal.objects.filter(user=request.user).delete()

        # for goal in goals:
        #     Goal.objects.create(user=request.user, name=goal)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.daily_goals = goals
        profile.save()

        return JsonResponse({"message": "Goals saved successfully"}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

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
    profiles = Profile.objects.filter(user=request.user)
    for profile in profiles:
        stack = profile.stack
        role = profile.role
        # print(stack)
    count = 0
    for i in stack:
        count += 1
    
    return render(request, 'profile.html', {'profile':profile, 'count':count, 'role':role})

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
    
# class DailyLogViewSet(viewsets.ModelViewSet):
#     queryset = DailyLog.objects.all()
#     serializer_class = DailyLogSerializer