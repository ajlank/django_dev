from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls", namespace="products")),
    path("auth/", include("authtokens.urls", namespace="authtokens")),
]
