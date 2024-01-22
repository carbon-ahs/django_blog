from django.urls import path

from . import views


# from .views import say_hello

urlpatterns = [
    path("", views.BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
]
