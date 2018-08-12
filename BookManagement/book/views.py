from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Book

def index(request):
    all_book_list = Book.objects.order_by('id')[:]
    template = loader.get_template('book/index.html')
    context = {
        'all_book_list': all_book_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    return HttpResponse("create a book ! ")

def read(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/read.html',{'book':book})

def delete(request):
    return HttpResponse("delete a book ! ")

def search(request):
    return HttpResponse("search books ! ")

