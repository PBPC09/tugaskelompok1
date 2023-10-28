from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from bookforum.models import ForumHead, ForumComment
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from datetime import datetime
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound, HttpResponseRedirect
from registerbook.models import Book
import json
#IMPORT BUAT USER PURA PURAAN
from django.contrib.auth.models import User
# USER_BARU = User(id = 1 , pk = 1, username="Bryan")
# USER_BARU.save()
# Create your views here.
@login_required(login_url='/login/')
def show_forum(request):
    questions = ForumHead.objects.all()
    comments = ForumComment.objects.all()
    context = {
        'user' : request.user,
        'name':request.user.username,
        'questions' : questions,
        'comments': comments,
    }
    return render(request, "forum.html", context)

@login_required(login_url='/login/')
@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        user = request.user
        # user = USER_BARU
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        question = request.POST.get('question')
        date = datetime.now()
        title = request.POST.get('title')
        new_question = ForumHead(user = user, book = book, date = date , title = title, question = question)
        result = {
            'pk' : new_question.pk,
            'fields' : {
                'username' : new_question.user.username,
                'title' : new_question.title,
                'question' : new_question.question,
                'date' : new_question.date,
                'book' : new_question.book.title,
            }
        }
        new_question.save()
        return JsonResponse(result)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
@csrf_exempt
def create_comments(request, pk):
    forum_head = ForumHead.objects.get(pk = pk)
    if request.method == 'POST':
        user = request.user
        # user = USER_BARU
        date = datetime.now()
        answer = request.POST.get('answer')
        new_comment = ForumComment(user = user, comment_to = forum_head, date = date, answer = answer)
        result = {
            'pk' : new_comment.pk,
            'fields' : {
                'username' : new_comment.user.username,
                'comment' : new_comment.answer,
                'date' : new_comment.date
            }
        }
        new_comment.save()
        return JsonResponse(result)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
@csrf_exempt
def delete_question(request, username, id):
    if request.method == 'GET' and request.user.username == username:
        ForumHead.objects.get(pk = id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
@csrf_exempt
def delete_comments(request, username, id):
    if request.method == 'GET' and request.user.username == username:
        ForumComment.objects.get(pk = id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

def show_forum_json_2(request):
    data = ForumHead.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')


def show_forum_json(request):
    models = ForumHead.objects.all()
    serialized_data = []
    for model in models:
        connected_comments = ForumComment.objects.filter(comment_to = model)
        comment_counts = len(connected_comments)
        book = model.book
        user = model.user
        model_data = {
            "model": "bookforum.forumhead",
            "pk": model.pk,  # Include the "pk" field
            "fields": {
                "book": book.title,
                "user": user.username,
                "date": str(model.date),  # Convert the date to a string
                "title": model.title,
                "question": model.question,
                "comment_counts" : comment_counts,
            }
        }
        serialized_data.append(model_data)
        # abis udah append ke serialized_data
    json_data = json.dumps(serialized_data)
    return HttpResponse(json_data, content_type="application/json")

def show_comments_json(request):
    data = ForumComment.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_uniquecomments_json(request, id):
    question = ForumHead.objects.get(pk = id)
    comments = ForumComment.objects.filter(comment_to=question)
    serialized_data = []
    for model in comments:
        user = model.user
        model_data = {
            "model": "bookforum.forumcomment",
            "pk": model.pk,  # Include the "pk" field
            "fields": {
                "user": user.username,
                "comment_to": model.comment_to.pk,
                "date": str(model.date),  # Convert the date to a string
                "answer" :  model.answer
            }
        }
        serialized_data.append(model_data)
        # abis udah append ke serialized_data
    json_data = json.dumps(serialized_data)
    return HttpResponse(json_data, content_type="application/json")

def show_books_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books), content_type="application/json")

@login_required(login_url='/login/')
def show_forumcomments(request, id_head):
    question = ForumHead.objects.get(pk = id_head)
    comments = ForumComment.objects.filter(comment_to=question)
    
    context = {
        'name' : request.user,
        'question': question,
        'comments': comments,
    }
    
    return render(request, "forumcomments.html", context)