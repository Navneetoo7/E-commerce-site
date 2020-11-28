from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="ShopHoame"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Trackingstatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Product"),
    path("checkout/", views.checkout, name="checkout"),
]