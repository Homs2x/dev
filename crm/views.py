from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

from . models import Info, Events

from django.contrib import messages

from rest_framework import viewsets

from .serializers import EventSerializer




# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('id')
    serializer_class = EventSerializer

def homepage(request):

    return render(request, 'crm/index.html')

def register(request):

    form = CreateUserForm()

    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():

                    form.save()

                    return redirect("my-login")
        
    context = {'registerform':form}

    return render(request, 'crm/register.html', context=context)

def my_login(request):

    form = LoginForm()

    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == "POST":

            form = LoginForm(request, data=request.POST)

            if form.is_valid():

                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None :

                    auth.login(request, user)

                    return redirect("dashboard")
        
    context = {'loginform':form}

    return render(request, 'crm/my-login.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("");

@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'crm/dashboard.html')

@login_required(login_url="my-login")
def org_info(request):
    if request.method == 'POST':
        orgName = request.POST['orgName']
        address = request.POST['address']
        contactInfo = request.POST['contactInfo']
        
        if orgName and address is not None:

            new_org = Info(org_name=orgName,address=address,contact_info=contactInfo)
            new_org.save()

            messages.success(request, 'Your organization was successfully registerd')
            return redirect('orglist')

    info = Info.objects.all()

    context = {'info':info}          

    return render(request, 'crm/orglist.html',context=context)

@login_required(login_url="my-login")
def reg_info(request):

    return render(request,'crm/registerorg.html')

@login_required(login_url="my-login")
def locate(request):

    return render(request, 'crm/locate.html')

@login_required(login_url="my-login")
def donate(request):

    return render(request, 'crm/donate.html')

@login_required(login_url="my-login")
def feedback(request):

    return render(request, 'crm/feedback.html')

@login_required(login_url="my-login")
def account(request):

    return render(request, 'crm/account.html')