from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    return HttpResponse("Hello, I Write other text here. You're at the polls profile.")
