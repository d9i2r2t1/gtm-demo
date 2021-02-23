from functools import wraps

from django.conf import settings
from django.contrib import messages

import requests


def check_recaptcha(func):
    """Проверка reCAPTCHA."""
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': request.POST.get('g-recaptcha-response')
            }
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data).json()
            if response['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
                messages.error(request, 'Необходимо пройти reCAPTCHA.')
        return func(request, *args, **kwargs)
    return wrapper
