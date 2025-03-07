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




def products(request):


def single_product(request):