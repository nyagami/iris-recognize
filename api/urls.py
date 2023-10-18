from django.urls import path
from . import views

urlpatterns = [
    path("verify/", views.verify, name="verify"),
    path("all_users/", views.get_all_users, name="get_all_users"),
]