from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def homepage(request):

    if request.method == 'GET':
        categories = Hero.objects.all()
        big = Hero_big.objects.get(title='We Are Damishop')
        men_products = Product.objects.filter(category='MN')
        wommen_products = Product.objects.filter(category='WN')
        kids_products = Product.objects.filter(category='KD')
        social_images = Social.objects.all()

        context = {
            'categories': categories,
            'men_products': men_products,
            'women_products': wommen_products,
            'kids_products':kids_products,
            'social_images': social_images,
            'big': big
        }
    else:
        subscriber_name = request.POST.get('name')
        subscriber_email = request.POST.get('email')
        subscriber = Subscriber(name=subscriber_name, email=subscriber_email)
        subscriber.save()
        return redirect('products')

    return render(request, 'Web/index.html', context)


def productspage(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'Web/products.html', context)

def single_productpage(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'single_product': product
    }
    return render(request, 'Web/single-product.html', context)