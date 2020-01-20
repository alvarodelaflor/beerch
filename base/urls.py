from django.contrib import admin
from django.urls import path
from myapp import views as myapp_view
from users import views as users_view

handler404 = 'myapp.views.my_custom_page_not_found_view'
handler500 = 'myapp.views.my_custom_page_500_error_view'

urlpatterns = [
    path('register', users_view.register),
    path('login', users_view.login),
    path('logout', users_view.logout),
    path('', myapp_view.index),
    path('admin/', admin.site.urls),
    path('indexRestaurants',myapp_view.indexRestaurants),
    path('restaurants', myapp_view.restaurants),
    path('users', myapp_view.users),
    path('users_filter', myapp_view.users_filter),
    path('reviews', myapp_view.reviews)
]
