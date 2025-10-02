from django.contrib import admin
from django.urls import path
from pages.views import HomeView, AboutView, ProductsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("products/", ProductsView.as_view(), name="products"),
]
