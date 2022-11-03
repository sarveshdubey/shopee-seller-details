from django.urls import path

from .views import SellerDetails_View

urlpatterns = [
    path('', SellerDetails_View.as_view(), name="Seller Details"),
]