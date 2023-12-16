from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'Event', views.EventViewSet)

urlpatterns = [


    
    path('', views.homepage, name=""),

    path('login-choice', views.login_choice, name="login-choice"),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

     path('my-login-staff', views.my_login_staff, name="my-login-staff"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('d',include(router.urls)),

    path('Event', include('rest_framework.urls', namespace='rest_framework')),

    path('user-logout', views.user_logout, name="user-logout"),

    path('registerorg', views.reg_info, name="registerorg"),

    path('orglist', views.org_info, name="orglist"),

    path('locate', views.locate, name="locate"),

    path('feedback', views.feedback, name="feedback"),

    path('account', views.account, name="account"),

    path('donate', views.donate, name="donate"),
]










