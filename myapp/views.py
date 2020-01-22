from django.shortcuts import render, redirect
from django.core.mail import send_mail
from base import settings
from myapp.populate import import_restaurants, import_reviews_users, find_url_reviews_from_user, import_reviews_restaurants
from myapp.auxiliar import SqliteConsults
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import Restaurant, User, Review
from django.db.models import Q
import urllib.parse
import urllib.request
import json


def index(request):
    return render(request, 'index.html', {'send_email': "no"})


def indexRestaurants(request):
    import_restaurants()
    import_reviews_users()
    #find_url_reviews_from_user()
    import_reviews_restaurants()
    return render(request, 'index.html', {'send_email': "no"})


def restaurants(request):
    data = request.POST.get('nameRestaurant', False)
    if data:
        restaurant_list = Restaurant.objects.filter(name__icontains=data)
    else:
        restaurant_list = Restaurant.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(restaurant_list, 4)
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)

    if data != '':
        placeholder = data    
    else:
        placeholder = 'Filtra por nombre del restaurante'
    return render(request, 'restaurants.html', { 'restaurants': restaurants, 'placeholder': placeholder })


def users(request):
    data = request.POST.get('username', False)
    if data:
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
        placeholder = data    
    else:
        placeholder = 'Filtra por nombre de usuario'
    return render(request, 'users.html', { 'users': users, 'placeholder': placeholder })


def user_profile(request):
    id = request.POST.get('id', False)
    users =  User.objects.filter(id=id)
    if len(users) > 0:
        user = users[0]
        reviews_list = Review.objects.filter(user=user)

        page = request.GET.get('page', 1)

        paginator = Paginator(reviews_list, 2)
        try:
            reviews = paginator.page(page)
        except PageNotAnInteger:
            reviews = paginator.page(1)
        except EmptyPage:
            reviews = paginator.page(paginator.num_pages)        
    else:
        user = None
        reviews = []
    return render(request, 'user.html', { 'user': user, 'reviews': reviews})          

def reviews(request):
    data = request.POST.get('search', False)
    if data:
        reviews_list = Review.objects.filter(Q(user__name__icontains=data) | Q(restaurant__name__icontains=data))
    else:
        reviews_list = Review.objects.all()    
    page = request.GET.get('page', 1)

    paginator = Paginator(reviews_list, 4)
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    if data:
        placeholder = data
    else:
        placeholder = 'Busque por nombre de usuario o restaurante'
    return render(request, 'reviews.html', { 'reviews': reviews, 'placeholder': placeholder })

def review_post(request):
    id = request.POST.get('id', False)
    reviews =  Review.objects.filter(id=id)
    if len(reviews) > 0:
        review = reviews[0]
    else:
        review = None
    return render(request, 'review.html', { 'review': review})


def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', {'exception': exception})


def my_custom_page_500_error_view(request):
    return render(request, '500.html')
