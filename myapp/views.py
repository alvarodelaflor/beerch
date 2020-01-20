from django.shortcuts import render, redirect
from django.core.mail import send_mail
from base import settings
from myapp.populate import import_restaurants, import_reviews_users
from myapp.auxiliar import SqliteConsults
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import Restaurant, User, Review
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
    restaurant_list = Restaurant.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(restaurant_list, 4)
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)

    return render(request, 'restaurants.html', { 'restaurants': restaurants })


def users(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'users.html', { 'users': users })

def users_filter(request):
    data = request.POST['username']
    if data != '':
        user_list = User.objects.filter(name__icontains=data)
    else:
        user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    if data != '':
        return render(request, 'users.html', { 'users': users, 'placeholder': data})    
    else:
        placeholder = 'Filtra por nombre de usuario'
        return render(request, 'users.html', { 'users': users, 'placeholder': placeholder })    

def reviews(request):
    reviews = SqliteConsults().ger_reviews_with_user_and_restaurant()
    reviews_list = Review.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(reviews_list, 4)
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    return render(request, 'reviews.html', { 'reviews': reviews })   


def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', {'exception': exception})


def my_custom_page_500_error_view(request):
    return render(request, '500.html')
