from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from products.models import Product, Category
from .forms import SearchForm
from .models import Setting, Contact ,ContactForm
from django.contrib import messages

from django.core.mail import send_mail

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk = 1)
    product_first = Product.objects.all().order_by('category')[:9]
    product_last = Product.objects.all().order_by('-id')[:9]
    product_random = Product.objects.all().order_by('?')[:9]
    context = {
        'setting':setting ,
        'product_first':product_first,
        'product_last': product_last,
        'product_random': product_random,
    }
    return render(request, 'hometemps/index.html',context)


def about(request):
    setting = Setting.objects.get(pk = 1)
    context = {

        'setting':setting
    }
    return render(request, 'hometemps/about.html',context)

def contact(request):
    if request.method == 'POST':    # if method is post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()  # creating relation with model

            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')  # take ip address of requested user
            data.save()  # save the data

            messages.success(request,'your message has been received.Thank you for your interest')
            # send email code goes here
            sender_name = form.cleaned_data['first_name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['test@gmail.com'])
            return HttpResponseRedirect('/contact')
    else:
        setting = Setting.objects.get(pk=1)
        form = ContactForm()
        context = {
            'setting':setting,'form':form
            }
        return render(request,'hometemps/contact.html',context)

def test(request):
    category = Category.objects.all()
    return render(request, 'hometemps/header.html',context={'category':category,
                                                            })

def catwise_product(request,id,slug):
    count = 0
    brand_product = Product.objects.filter(category_id=id)
    for c in brand_product:
        count += count
        print(count)
    products = Product.objects.filter(category__parent_id=id)
    context = {
        'products':products,
        'brand_product':brand_product,
        'count':count
    }
    return render(request,'product_temps/category.html',context)

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # catid = form.cleaned_data['catid']

            search_prod = Product.objects.filter(keywords__icontains=query)
            context = {
                'serach_prod':search_prod
            }
            return render(request,'product_temps/search.html',context)
        else:
            return HttpResponse('something went wrong')
    return HttpResponse('/')