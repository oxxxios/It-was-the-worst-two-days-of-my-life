from django.urls import path, include
from products.views import ProductsListView, ProductDetailView, CategoryViewSet, ReviewViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"category", CategoryViewSet)
router.register(r"review", ReviewViewSet)



urlpatterns = [
    path("products/", ProductsListView.as_view()),
    path("products/<int:id>/", ProductDetailView.as_view()),
    path("", include(router.urls))
]