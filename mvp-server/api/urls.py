from rest_framework import routers
from .views import CategoryViewSet, StoreViewSet, OrderViewSet
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'stores', StoreViewSet, basename='store')
router.register(r'orders', OrderViewSet, basename='order')

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
]
