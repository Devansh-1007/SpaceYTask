from django.urls import path
from billing_counter import views

urlpatterns = [path("", views.index, name="index")]
