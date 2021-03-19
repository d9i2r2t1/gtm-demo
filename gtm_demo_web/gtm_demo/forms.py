import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms
from django.conf import settings

from gtm_demo.models import DemoLanding

log = logging.getLogger(__name__)


class GtmDemoLandingCreationForm(forms.ModelForm):
    class Meta:
        model = DemoLanding
        fields = '__all__'
        labels = {
            'gtm_id': 'Идентификатор контейнера GTM:'
        }
        widgets = {
            'gtm_id': forms.TextInput(attrs={
                'data-toggle': 'tooltip',
                'data-placement': 'right',
                'title': 'Идентификатор должен быть вида "GTM-XXXXXXX". '
                         'Найти его можно вверху страницы созданного '
                         'контейнера.',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'gtm_demo_landing_creation_form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'gtm_id',
            HTML(
                f'<div class="form-group"><div class="g-recaptcha" '
                f'data-sitekey="{settings.GOOGLE_RECAPTCHA_SITE_KEY}">'
                f'</div></div>'),
        )
