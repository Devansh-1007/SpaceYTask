from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("billing_counter/", include("billing_counter.urls")),
    path("admin/", admin.site.urls),
]
