from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def create(request):
    return HttpResponse("create a book ! ")

def read(request):
    return HttpResponse("read a book ! ")

def delete(request):
    return HttpResponse("delete a book ! ")

def search(request):
    return HttpResponse("search books ! ")

