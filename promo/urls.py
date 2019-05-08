from django.urls import path
from promo.views import PromoIndexView

urlpatterns = [
    path('promo/', PromoIndexView.as_view(), name="promo_page"),
]