from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_update_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # * long way to produce 404
    # try:
    #     obj = Product.objects.get(id=id)
    # except:
    #     raise Http404

    my_form = ProductForm(request.POST or None, instance=obj)
    if my_form.is_valid():
        # now the data is good
        my_form.save()

    context = {
        'form': my_form

    }
    return render(request, 'products/product_create.html', context)


def product_list_view(request):
    queryset = Product.objects.all()  # List of objects
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_details.html', context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == 'POST':
      # Confirming delete
        obj.delete()
        return redirect('../../')
    context = {

    }
    return render(request, 'products/product_delete.html', context)


# def dynamic_lookup_view(request, id):
#     # obj = Product.objects.get(id=id)
#     obj = get_object_or_404(Product, id=id)
#     # * long way to produce 404
#     # try:
#     #     obj = Product.objects.get(id=id)
#     # except:
#     #     raise Http404

#     context = {
#         'object': obj
#     }
#     return render(request, 'products/product_details.html', context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         # Product.objects.create(title=my_new-title)
#         print(my_new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)


# def render_initial_data(request):
#     initial_data = {
#         'title': 'This is my awesome title'
#     }
#     obj = Product.objects.get(id=2)
#     form = ProductForm(request.POST or None,
#                        #  initial=initial_data,
#                        instance=obj)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)
