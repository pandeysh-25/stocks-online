from django.shortcuts import render

# Create your views here.

from signup.models import signup
def signup_1(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        phoneno=request.POST["phone"]
        city=request.POST["city"]
        som=request.POST["som"]

        lst=signup()
        lst.username=username
        lst.password=password
        lst.phoneno=phoneno
        lst.city=city
        lst.som=som
        lst.save()
        return render(request,'welcome.html')
    else:
        return render(request,'signup.html')

def home(request):
    return render(request, 'stocks.html')

def myhome(request):
    if login_check==True:
        return render(request, 'myhome.html')
    else:
        return render(request,'login.html')


