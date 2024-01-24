from django.urls import path

from . import views


# from .views import say_hello

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
