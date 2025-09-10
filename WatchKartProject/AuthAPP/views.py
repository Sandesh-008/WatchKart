from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = "AuthAPP/register.html"
    context = {'form': form}
    return render(request, template_name, context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display-watch')
    template_name = "AuthAPP/login.html"
    context = {}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')