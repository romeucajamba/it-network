from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create_user(request):
    return HttpResponse("User created successfully")
