from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the index page of the poll site.")


def detail(request, question_id):
    return HttpResponse(f'This is question with the id: {question_id}')


def results(request, question_id):
    response = "Here are the results of the question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')
