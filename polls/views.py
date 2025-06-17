from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def profile(request):
    return HttpResponse("Hello, I Write other text here. You're at the polls profile.")

def contact(request):
    return HttpResponse("Please contact me at 085759402332")
