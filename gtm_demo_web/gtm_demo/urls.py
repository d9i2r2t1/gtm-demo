from django.urls import path

from gtm_demo.decorators import check_recaptcha
from gtm_demo.views import MainView, DemoLandingView

app_name = 'gtm_demo'

urlpatterns = [
    path('', check_recaptcha(MainView.as_view()), name='main'),
    path('<slug:hashcode>/', DemoLandingView.as_view(), name='demo_landing'),
]
