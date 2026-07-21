from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

# /products -> index
# Uniform Resource Locator (Address)

def index(request):
    return HttpResponse(f"Products in database: {Product.objects.count()}")


def new(request):
    return HttpResponse('New Products')



