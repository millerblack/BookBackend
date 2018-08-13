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

def create(request, book_id, book_name, book_author):
    try:
        new_book = Book(book_id=book_id, book_name=book_name, book_author=book_author)
        new_book.save()
    except:
        raise Http404("Book is not be created")
    return HttpResponse("Create a book successfully! id:%s, name:%s , author: %s" % (book_id, book_name, book_author))

def read_id(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/read.html',{'book':book})

def read_name(request, book_name):
    try:
        book = Book.objects.get(book_name=book_name)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'book/read.html',{'book':book})

def delete(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book.delete()
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return HttpResponse("delete a book ! book_id: %s" % book_id)

def search(request, book_name):
    all_book_list = Book.objects.order_by('id')[:]
    include_name_list = []
    if book_name == "*":
        include_name_list = all_book_list
    else:
        for each_book in all_book_list:
            if book_name in each_book.book_name:
                include_name_list.append(each_book)
    template = loader.get_template('book/index.html')
    context = {
        'include_name_list': include_name_list,
    }
    return HttpResponse(template.render(context, request))

