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
        book = request.POST.get('book')
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
                'date' : new_question.date
            }
        }
        new_question.save()
        return JsonResponse(result)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
@csrf_exempt
def create_comments(request, pk):
    forum_head = ForumHead.objects.filter(pk = pk)
    if request.method == 'POST':
        user = request.user
        # user = USER_BARU
        comment_to = forum_head 
        date = datetime.now()
        answer = request.POST.get('answer')

        new_comment = ForumComment(user = user, comment_to = comment_to, date = date, answer = answer)
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
def delete_question(request, id):
    if request.method == 'DELETE':
        ForumHead.objects.get(pk = id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/login/')
@csrf_exempt
def delete_comments(request, id):
    if request.method == 'DELETE':
        ForumComment.objects.get(pk = id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

def show_forum_json(request):
    data = ForumHead.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_comments_json(request):
    data = ForumComment.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')