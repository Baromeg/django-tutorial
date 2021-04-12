from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):  # *rgs, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1>Hello World</h1>')  # string of HTML code
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):  # *rgs, **kwargs
    # return HttpResponse('<h1>Contact page</h1>')  # string of HTML code
    return render(request, 'contact.html', {})


def projects_view(request, *args, **kwargs):  # *rgs, **kwargs
    # return HttpResponse('<h1>Projects page</h1>')  # string of HTML code
    return render(request, 'projects.html', {})


def about_view(request, *args, **kwargs):  # *rgs, **kwargs
    my_context = {
        'my_text': 'this is about us',
        'my_number': 123,
        'my_list': [123, 3212, 32, 1]
    }

    return render(request, 'about.html', my_context)
