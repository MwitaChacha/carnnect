from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .utils import Calendar
from django.views import generic
from django.utils.safestring import mark_safe
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all().order_by('-posted_at')
    advice = Advice.objects.all().order_by('-posted_at')
    respos = Response.objects.all().filter().order_by('-posted_at')
    current_user = request.user
    form = ResponseForm()
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(user=current_user)

    except ObjectDoesNotExist:
        return redirect('update_profile')
    profiles = Profile.objects.filter(user_id=current_user.id).all()
    if request.method == 'POST':
        form = ResponseForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    else:
        form = ResponseForm()
    return render(request, 'index.html', {'profiles': profiles, 'posts': posts, 'advice': advice, 'form': form, 'respos': respos, 'current_user': current_user})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect('index')
        else:
            form = ProfileForm()
    return render(request, 'update-profile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request, pk):
    user = User.objects.get(pk=pk)
    profiles = Profile.objects.filter(user=user).all()
    current_user = request.user
    return render(request, 'profile.html', {"current_user": current_user, "user": user, "profiles": profiles})


def about(request):
    user = request.user
    profiles = Profile.objects.filter(user=user).all()
    return render(request, 'about.html', {'profiles': profiles})


def tips(request):
    user = request.user
    profiles = Profile.objects.filter(user=user).all()
    return render(request, 'tips.html', {'profiles': profiles})


@login_required(login_url='/accounts/login/')
def issue(request):
    user = request.user
    profiles = Profile.objects.filter(user=user).all()
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            issu = form.save(commit=False)
            issu.user = request.user
            issu.save()
            return redirect ('mechanical_issue')        
        else:
            form = PostForm()
    return render(request, 'issue.html', {'form': form, 'profiles': profiles})


