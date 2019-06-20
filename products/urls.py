from django.urls import path
from .views import *


urlpatterns = [
    path('categories', categories),
    path('categories/<categoryName>', categoryDisplay),
    path('productDisplay/<productId>', productDisplay),
    path('search', search),
    path('cart', cart),
]
