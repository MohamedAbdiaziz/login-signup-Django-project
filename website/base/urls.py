from django.urls import path,include
from .views import home,signup,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path('logout/', logout_view, name='Logout'),
    path("accounts/signup/", signup,name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]
