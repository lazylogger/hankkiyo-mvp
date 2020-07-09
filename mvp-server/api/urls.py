from rest_framework import routers
from .views import CategoryViewSet, StoreViewSet
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'stores', StoreViewSet, basename='store')

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
]
