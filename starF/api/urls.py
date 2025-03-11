from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, CategoryViewSet

# Router ile API'leri tanımlıyoruz
router = DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'category', CategoryViewSet)

# URL'leri router ile yönlendirmek
urlpatterns = router.urls
