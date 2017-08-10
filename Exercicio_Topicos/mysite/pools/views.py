from django.shortcuts import render
from .models import Question, Choice

# Create your views here.


def index(request):
    questions = Question.objects.order_by('-pub_date')
    contexto = {'questions': questions}

    return render(request, 'index.html', contexto)


def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    contexto = {'question': question, 'choices': choices}

    return render(request, 'question.html', contexto)


def results(request, question_id):
    pass


def vote(request, question_id):
    pass


def manage(request):
    pass