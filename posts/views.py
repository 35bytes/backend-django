# Django
from django.shortcuts import render
from django.http import HttpResponse

def list_posts(request):
    posts = [1, 2, 3, 4]
    return HttpResponse(str(posts))