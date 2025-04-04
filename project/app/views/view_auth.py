from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.cache import cache
from ..forms import UserCreationForm
from app.models import User

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if 'next' in request.GET:
        messages.warning(request, 'Anda harus login terlebih dahulu')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Username atau password salah')
        else:
            messages.error(request, 'Username atau password salah')
    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan! Silakan pilih username lain.")
        elif form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registrasi berhasil. Anda telah login.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Terjadi kesalahan saat registrasi. Silakan periksa kembali data Anda.')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
