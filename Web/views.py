from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def homepage(request):

    if request.method == 'GET':
        categories = Hero.objects.all()
        men_products = Product.objects.filter(category='MN')
        wommen_products = Product.objects.filter(category='WN')
        kids_products = Product.objects.filter(category='KD')
        social_images = Social.objects.all()

        context = {
            'categories': categories,
            'men_products': men_products,
            'women_products': wommen_products,
            'kids_products':kids_products,
            'social_images': social_images
        }
    else:
        subscriber_name = request.POST.get('name')
        subscriber_email = request.POST.get('email')
        subscriber = Subscriber(name=subscriber_name, email=subscriber_email)
        subscriber.save()

    return render(request, 'web/index.html', context)


# def products(request):


# def single_product(request):