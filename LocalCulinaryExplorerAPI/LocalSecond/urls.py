from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChefProfileViewSet, IngredientViewSet, FoodViewSet, FoodRateViewSet, login_view  # Import your custom login view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chefs', ChefProfileViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'food', FoodViewSet)
router.register(r'ratings', FoodRateViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('api-token-auth/', login_view, name='api_token_auth'),  
]
