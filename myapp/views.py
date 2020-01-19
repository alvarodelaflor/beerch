from django.shortcuts import render, redirect
from django.core.mail import send_mail
from base import settings
import urllib.parse
import urllib.request
import json


def index(request):
    return render(request, 'index.html', {'send_email': "no"})


def cv(request):
    return render(request, 'cv.html')


def cv2(request):
    return render(request, 'cv2.html')


def post(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    if email is None:
        email = 'Anonimo'
    message = request.POST.get('message')
    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY, 'response': recaptcha_response}
    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    if recaptcha_response is not "":
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        if result['success']:
            if email is not 'Anonimo':
                send_mail(
                    '¡Hola ' + name + '! (alvarodelaflor.com)',
                    'Aquí tiene el correo copia que envió en el portal: ' + email + "\n\n" +
                    message,
                    email,
                    [email],
                )
            send_mail(
                'Correo del portal - ' + name,
                'Correo de contacto: ' + email + "\n" + message,
                email,
                ['alvarodelaflor@gmail.com'],
            )
            return render(request, 'index.html', {'send_email': "yes"})
    else:
        return render(request, 'index.html', {'hack': "yes"})


def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', {'exception': exception})


def my_custom_page_500_error_view(request):
    return render(request, '500.html')
