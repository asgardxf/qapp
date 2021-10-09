import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .models import Client, Quest

defaultHeaders = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

def createJsonResponse(obj, plainFields, customFields):
  fieldsList = plainFields.split(' ')
  res = []
  for o in obj:
    cur = {}
    for f in fieldsList:
        cur[f] = getattr(o, f)
    for f in customFields:
        cur[f] = customFields[f](o)
    res.append(cur)
  j = json.dumps(res)
  return HttpResponse(j, headers=defaultHeaders)

def index(req):
  return HttpResponse('my index')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.

def quest_list(request):
    obj = Quest.objects.select_related('partner').all()
    customFields = dict(
        partner_name=lambda o: o.partner.name,
        photo=lambda o: o.photo.url,
    )
    return createJsonResponse(obj, 'name',customFields)

def createUser(request):
    if request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(request.POST['username'], None, request.POST['password1'])
        client = Client.objects.create(user=user, contact=request.POST['username'])
        return redirect('../login')
    return HttpResponse("Ошибка создания")


urlMap = dict(
  quest_list=quest_list,
)