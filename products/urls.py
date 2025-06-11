from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import ProductCategoryListView, MakerListView, ProductListView

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("categories", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers", MakerListView.as_view(), name="makers-list"),
]
