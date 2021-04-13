from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # * long way to produce 404
    # try:
    #     obj = Product.objects.get(id=id)
    # except:
    #     raise Http404

    context = {
        'object': obj
    }
    return render(request, 'products/product_details.html', context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form

#     }
#     return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         # Product.objects.create(title=my_new-title)
#         print(my_new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)


def render_initial_data(request):
    initial_data = {
        'title': 'This is my awesome title'
    }
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None,
                       #  initial=initial_data,
                       instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_details.html', context)
