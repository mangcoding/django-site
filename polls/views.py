from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ""
    for q in latest_question_list:
        output += f"{q.question_text}<br>"
        #answer list
        answer_list = Choice.objects.filter(question=q)
        list_answer = ", ".join([a.choice_text for a in answer_list])
        output += f"Pilihan: {list_answer}"
        output += "<br><br>"
    return HttpResponse(output)

def html_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    answer_list = Choice.objects.all()
    context = {
        "latest_question_list": latest_question_list,
        "answer_list": answer_list
    }
    return render(request, "index.html", context)

def profile(request):
    return HttpResponse("Hello, I Write other text here. You're at the polls profile.")

def contact(request):
    return HttpResponse("Please contact me at 085759402332")
