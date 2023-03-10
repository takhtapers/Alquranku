from content.models import Artikel,Doa,Alquran
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from content.models import Artikel
from users.models import Biodata
import requests

def home(request):
    template_name = 'front/home.html'
    context = {
        'title':'my home',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about-us.html'
    context = {
        'title':'my about',
        'welcome':'welcome my about',
    }
    return render(request, template_name, context)

def alquran(request):
    template_name = 'front/alquran.html'
    alquran = Alquran.objects.all()
    context = {
        'title':'my blog',
        'alquran':alquran
    }
    return render(request, template_name, context)
def doa(request):
    template_name = 'front/doa.html'
    doa = Doa.objects.all()
    context = {
        'title':'my blog',
        'doa':doa
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact-us.html'
    context = {
        'title':'my contact',
        'welcome':'welcome my contact',
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)