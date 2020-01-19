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
    path('welcome', users_view.welcome),
    path('', myapp_view.index),
    path('cv', myapp_view.cv),
    path('curriculumvitae', myapp_view.cv),
    path('curriculumVitae', myapp_view.cv),
    path('CurriculumVitae', myapp_view.cv),
    path('Curriculumvitae', myapp_view.cv),
    path('post', myapp_view.post),
    path('admin/', admin.site.urls),
]
