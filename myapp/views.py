from django.shortcuts import render, redirect
from django.core.mail import send_mail
from base import settings
from myapp.populate import import_restaurants, import_reviews_users
from myapp.auxiliar import SqliteConsults
import urllib.parse
import urllib.request
import json


def index(request):
    return render(request, 'index.html', {'send_email': "no"})

def indexRestaurants(request):
    import_restaurants()
    import_reviews_users()
    return render(request, 'index.html', {'send_email': "no"})

def restaurants(request):
    restaurants = SqliteConsults().get_restaurants()
    return render(request, 'restaurants.html', {'restaurants': restaurants})

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', {'exception': exception})


def my_custom_page_500_error_view(request):
    return render(request, '500.html')
