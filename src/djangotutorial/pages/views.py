from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(*args, **kwargs):  # *rgs, **kwargs
    return HttpResponse('<h1>Hello World</h1>')  # string of HTML code


def contact_view(*args, **kwargs):  # *rgs, **kwargs
    return HttpResponse('<h1>Contact page</h1>')  # string of HTML code
