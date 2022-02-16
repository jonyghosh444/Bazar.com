# Hare krishna

from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index, name="ShopHome"),
    path("about/", views.About, name="AboutUs"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.Tracker, name="Tracker"),
    path("search/", views.Search, name="Search"),
    path("product/<int:myid>", views.ProductView, name="ProductView"),
    path("checkout/", views.Checkout, name="CheckOut"),
]