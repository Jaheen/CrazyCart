from django.shortcuts import render
from django.db.models import Q

from .models import *


def categories(request):
    context = {
        "Categories" : Categories.objects.all()
    }
    return render(request, "products/categories.html", context)

def categoryDisplay(request, categoryName):
    print(categoryName)
    context = {
        "CategoryName" : categoryName,
        "Products" : Products.objects.filter(productCategory=Categories.objects.get(categoryName=categoryName))
    }
    return render(request, "products/categoryDisplay.html", context)

def productDisplay(request, productId):
    product = Products.objects.get(productId = productId)
    context = {
        "Product" : product
    }
    return render(request, "products/productDisplay.html", context)

# Use Q clas to make multiple queries across multiple fields
def search(request):
    queryString = request.GET.get("queryString")
    results = Products.objects.filter(
        Q(productName__icontains=queryString)    |
        Q(productCategory__categoryName__icontains=queryString)    |
        Q(productDescriptions__icontains=queryString)    |
        Q(productSpecifications__icontains=queryString)
    )
    context = {
        "QueryString" : queryString,
        "Results" : results
    }
    return render(request, "products/searchPage.html", context)

def cart(request):
    return render(request, "products/cart.html")
