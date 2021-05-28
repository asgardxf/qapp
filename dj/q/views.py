from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createUser(request):
    if request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(request.POST['username'], None, request.POST['password1'])
        return redirect('../login')
    return HttpResponse("Ошибка создания")