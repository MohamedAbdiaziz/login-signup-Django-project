from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



@login_required
# Create your views here.
def home(request):
    return render(request,"base/index.html")


def signup(request):
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})