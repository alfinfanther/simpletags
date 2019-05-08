from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PromoIndexView(TemplateView):
    template_name = 'promo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = "Sandal Jepit"
        return context
