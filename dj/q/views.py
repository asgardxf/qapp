import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .models import Client, Quest, City, Order, Discount, Cert


from django.views.decorators.csrf import csrf_exempt

defaultHeaders = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

def createJsonResponse(obj, plainFields, customFields = {}):
  fieldsList = plainFields.split(' ')
  res = []
  for o in obj:
    cur = {}
    for f in fieldsList:
        cur[f] = getattr(o, f)
    for f in customFields:
        cur[f] = customFields[f](o)
    res.append(cur)
  j = json.dumps(res, ensure_ascii=False, default=str)
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
        timeslot_list=lambda o: [item.text for item in o.timeslot_list.all()],
        city=lambda o: o.city.id,
    )
    return createJsonResponse(obj, 'name id price blocked position', customFields)

def city_list(request):
    obj = City.objects.all()
    return createJsonResponse(obj, 'name id')

def order_list(request):
    obj = Order.objects.all()
    return createJsonResponse(obj, 'date timeslot', dict(
      quest=lambda o: o.quest.id,
      client=lambda o: o.client.id,
    ))
def discount_list(request):
    obj = Discount.objects.all()
    return createJsonResponse(obj, 'date timeslot', dict(
      quest=lambda o: o.quest.id,
    ))
def client_list(request):
    obj = Client.objects.all()
    return createJsonResponse(obj, 'name cashback contact id pw email')
def cert_list(request):
    obj = Cert.objects.all()
    return createJsonResponse(obj, 'code', dict(
      quest=lambda o: o.quest.id,
    ))

def createUser(request):
    if request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(request.POST['username'], None, request.POST['password1'])
        client = Client.objects.create(user=user, contact=request.POST['username'])
        return redirect('../login')
    return HttpResponse("Ошибка создания")
@csrf_exempt
def createClient(request):
    obj = Client.objects.filter(contact=request.GET.get('contact'))
    if (len(obj) != 0):
      return HttpResponse('{"error":1}', headers=defaultHeaders)
    client = Client.objects.create(contact=request.GET.get('contact'), name='', pw=request.GET.get('password'), email=request.GET.get('email'))
    return createJsonResponse([client], 'id')

def creteCert(request):
    Cert.objects.create(quest_id=request.POST['quest'], code=request.POST['code'])
    #Cert.objects.create(quest_id=1, code='123')
    return HttpResponse("ok")
urlMap = dict(
  quest_list=quest_list,
  city_list=city_list,
  order_list=order_list,
  discount_list=discount_list,
  client_list=client_list,
  create_cert=creteCert,
  create_client=createClient,
)

#