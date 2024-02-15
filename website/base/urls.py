from django.urls import path,include
from .views import home,signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path("accounts/signup/", signup,name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]
