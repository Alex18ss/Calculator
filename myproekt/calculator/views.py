from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'calculator/index.html')


def rand_gen(request):
    return HttpResponse('<h4>Random generator</h4>')


def timer(request):
    return HttpResponse('<h4>Timer</h4>')
