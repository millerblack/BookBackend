from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

import json

from .models import Book

def test(request):
    all_book_list = Book.objects.order_by('id')[:]
    template = loader.get_template('book/test.html')
    context = {
        'all_book_list': all_book_list,
    }
    return HttpResponse(template.render(context, request))


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
        book_dict = {'book_id': book_id, 'book_name': book_name, 'book_author':book_author}
        request_result = book_dict
        status = 'success'
    except:
        status = 'failure'
        request_result = 'Book is not be created.'
    request_feedback = {'status': status, 'request_result': request_result}
    json_request_feedback = json.dumps(request_feedback, sort_keys=True, indent=4)
    return HttpResponse(json_request_feedback)

def read_id(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book_dict = {'book_id': book.book_id, 'book_name': book.book_name, 'book_author':book.book_author}
        request_result = book_dict
        status = 'success'
    except Book.DoesNotExist:
        status = 'failure'
        request_result = 'Book does not exist'
    request_feedback = {'status': status, 'request_result': request_result}
    json_request_feedback = json.dumps(request_feedback, sort_keys=True, indent=4)
    return HttpResponse(json_request_feedback)

def read_name(request, book_name):
    try:
        book = Book.objects.get(book_name=book_name)
        book_dict = {'book_id': book.book_id, 'book_name': book.book_name, 'book_author':book.book_author}
        request_result = book_dict
        status = 'success'
    except Book.DoesNotExist:
        status = 'failure'
        request_result = 'Book does not exist'
    request_feedback = {'status': status, 'request_result': request_result}
    json_request_feedback = json.dumps(request_feedback, sort_keys=True, indent=4)
    return HttpResponse(json_request_feedback)

def delete(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book.delete()
        status = 'success'
        request_result = 'Deleted books id: %s' % book_id
    except Book.DoesNotExist:
        status = 'failure'
        request_result = 'Book does not exist'
    request_feedback = {'status': status, 'request_result': request_result}
    json_request_feedback = json.dumps(request_feedback, sort_keys=True, indent=4)
    return HttpResponse(json_request_feedback)

def search(request, book_name):
    all_book_list = Book.objects.order_by('id')[:]
    include_name_list = []
    if book_name == "*":
        include_name_list = all_book_list
    else:
        for each_book in all_book_list:
            if book_name in each_book.book_name:
                include_name_list.append(each_book)
    book_dict_list = []
    for each_book in include_name_list:
        book_dict = {'book_id': each_book.book_id, 'book_name': each_book.book_name, 'book_author':each_book.book_author}
        book_dict_list.append(book_dict)
    status = 'success'
    request_result = book_dict_list
    request_feedback = {'status': status, 'request_result': request_result}
    json_request_feedback = json.dumps(request_feedback, sort_keys=True, indent=4)
    return HttpResponse(json_request_feedback)
