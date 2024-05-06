from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth import get_user_model


auth_user = get_user_model()

# Create your views here.
def index(request):
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")

def home(request):
   return render(request,"home.html")


def register(request):
  if request.method == 'POST':
      username = request.POST.get('user_name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      # print(password,confirm_password,"............")

      if password != confirm_password:
          return JsonResponse({'res': 'failed', 'msg': 'Passwords do not match'})

      if User.objects.filter(email=email).exists():
          return JsonResponse({'res': "failed", 'msg': 'Email already exists'})

      hashed_password = make_password(password)
      user = User.objects.create(username=username, email=email, password=hashed_password)
      return JsonResponse({'res': "success", 'msg': 'Signup successful'})
  else:
      return JsonResponse({'res': "failed", 'msg': 'Invalid request'})



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'res': 'success', 'msg': 'Login successful'})
        else:
            return JsonResponse({'res': 'failed', 'msg': 'Invalid credentials'})
    else:
        return JsonResponse({'res': 'failed', 'msg': 'Invalid request'})
