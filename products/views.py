from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Genre, Product, Category,Images


def product(request,id,slug):
    product = Product.objects.filter(id=id,slug=slug)
    images =Images.objects.filter(product_id=id)
    context ={
        'product':product,
        'images':images
    }
    return render(request,'product_temps/product.html',context)


def show_genres(request):
    return render(request, "genre.html", {'genres': Genre.objects.all()})

# def catwise_product(request,id,slug):
#     products = Product.objects.filter(category__parent_id=id)
#     return render(request,'product_temps/category.html',{'products':products})