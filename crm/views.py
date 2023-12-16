from django.shortcuts import render, redirect

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from . models import Info, Events

from django.contrib import messages

from rest_framework import viewsets

from .serializers import EventSerializer

from .forms import DonatorAuthenticationForm, MyRegistrationForm, MyUserCreationForm, MyAuthenticationForm, CustomAuthenticationForm,DonatorRegistrationForm, StaffRegistrationForm



# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('id')
    serializer_class = EventSerializer

def homepage(request):

    return render(request, 'crm/index.html')

from django.contrib.auth import login

from django.contrib import messages

def register(request):
    form = MyRegistrationForm()

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            form = MyRegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                status = form.cleaned_data.get('status')

                # Initialize user_form based on the chosen status
                if status == 'donator':
                    user_form = DonatorRegistrationForm(request.POST)
                elif status == 'manager':
                    user_form = StaffRegistrationForm(request.POST)

                if user_form.is_valid():
                    user = user_form.save(commit=False)
                    user.username = username
                    user.status = status  # Set the status field
                    user.save()

                    # Log in the user immediately after registration
                    login(request, user)

                    # Redirect based on user status
                    if status == 'donator':
                        return redirect("donate")
                    elif status == 'manager':
                        return redirect("dashboard")
                else:
                    messages.error(request, 'Invalid registration details.')

    context = {'registerform': form}
    return render(request, 'crm/register.html', context=context)




def my_login(request):
    form = DonatorAuthenticationForm()

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = DonatorAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None and user.status == 'donator':
                login(request, user)
                return redirect("donate")

    context = {'loginform': form}
    return render(request, 'crm/my-login.html', context=context)


def my_login_staff(request):
    form = CustomAuthenticationForm()

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None and user.status == 'manager':
                login(request, user)
                return redirect("dashboard")

    context = {'loginforms': form}
    return render(request, 'crm/my-login-staff.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("");

@login_required(login_url="my-login-staff")
def dashboard(request):

    return render(request, 'crm/dashboard.html')

@login_required(login_url="my-login")
def org_info(request):

    info = Info.objects.all()

    context = {'info':info}          

    return render(request, 'crm/orglist.html',context=context)

@login_required(login_url="my-login")
def reg_info(request):

    if request.method == 'POST':
        orgName = request.POST['orgName']
        address = request.POST['address']
        contactInfo = request.POST['contactInfo']
        
        if orgName and address is not None:

            new_org = Info(org_name=orgName,address=address,contact_info=contactInfo)
            new_org.save()

            messages.success(request, 'Your organization was successfully registerd')
            return redirect('registerorg')

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

def login_choice(request):

    if request.method == 'POST':
        login_type = request.POST.get('login_type')

        if login_type == 'staff':
            return redirect('my-login-staff')
        elif login_type == 'donator':
            return redirect('my-login')
    return render(request, 'crm/login-choice.html')