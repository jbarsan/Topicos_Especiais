from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    question = Question.objects.all()
    return render(request, 'index.html',
                  {'questions': question})

def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question.html',
                  {'question': question})