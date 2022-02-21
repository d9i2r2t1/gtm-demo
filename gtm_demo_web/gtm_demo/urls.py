from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from gtm_demo.decorators import check_recaptcha
from gtm_demo.views import MainView, DemoLandingView

app_name = 'gtm_demo'

urlpatterns = [
    path('', ensure_csrf_cookie(check_recaptcha(MainView.as_view())), name='main'),
    path('<slug:hashcode>/', DemoLandingView.as_view(), name='demo_landing'),
]
