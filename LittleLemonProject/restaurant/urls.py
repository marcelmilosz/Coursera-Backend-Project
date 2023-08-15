from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    # Api
    path("api/menu/", views.MenuView.as_view(), name="menu-list"),
    path("api/menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-single"),
]
