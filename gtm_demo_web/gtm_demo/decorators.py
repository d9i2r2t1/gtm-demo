import logging
from functools import wraps

from django.conf import settings
from django.contrib import messages

import requests

log = logging.getLogger(__name__)


def check_recaptcha(func):
    """Проверка reCAPTCHA."""

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == "POST":
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": request.POST.get("g-recaptcha-response"),
            }
            try:
                response = requests.post(
                    "https://www.google.com/recaptcha/api/siteverify", data=data
                ).json()
            except Exception as e:
                log.warning(f"Failed to validate reCAPTCHA: {e}")
                request.recaptcha_is_valid = True
            else:
                if response["success"]:
                    request.recaptcha_is_valid = True
                else:
                    request.recaptcha_is_valid = False
                    messages.error(request, "Необходимо пройти reCAPTCHA.")
        return func(request, *args, **kwargs)

    return wrapper
