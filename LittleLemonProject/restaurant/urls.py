from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    # Api - Menu
    path("api/menu/", views.MenuView.as_view(), name="menu-list"),
    path("api/menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-single"),
    # Api - Booking
    path("api/booking/", views.BookingView.as_view(), name="booking-list"),
    path(
        "api/booking/<int:pk>",
        views.SingleBookingItemView.as_view(),
        name="booking-single",
    ),
    path("api-token-auth/", obtain_auth_token),
]
