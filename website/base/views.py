from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout




@login_required
# Create your views here.
def home(request):
    return render(request,"base/index.html")


def signup(request):
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('/') 