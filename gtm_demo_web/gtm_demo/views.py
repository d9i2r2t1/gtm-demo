import logging

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from gtm_demo.forms import GtmDemoLandingCreationForm
from gtm_demo.models import DemoLanding

log = logging.getLogger(__name__)


class MainView(CreateView):
    form_class = GtmDemoLandingCreationForm
    template_name = "gtm_demo/main_page.html"

    object = None

    def get_success_url(self):
        return reverse_lazy("gtm_demo:demo_landing", args=(self.object.hashcode,))

    def form_valid(self, form):
        if not self.request.recaptcha_is_valid:
            return super().form_invalid(form)
        self.object, _ = DemoLanding.objects.get_or_create(
            gtm_id=form.cleaned_data["gtm_id"].upper()
        )
        return HttpResponseRedirect(self.get_success_url())


class DemoLandingView(DetailView):
    model = DemoLanding
    slug_field = "hashcode"
    slug_url_kwarg = "hashcode"
    template_name = "gtm_demo/demo_landings/landing_1.html"
    context_object_name = "demo_landing"
