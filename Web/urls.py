from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', productspage, name='products'),
    path('singleproduct/', single_productpage, name='singleproduct')
]