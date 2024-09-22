from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, ChefProfile, Ingredient, Food, FoodRate
from .serializers import UserSerializer, ChefProfileSerializer, IngredientSerializer, FoodSerializer, FoodRateSerializer
from .permissions import IsAdmin, IsUser, IsChef
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Token

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.token})
        return JsonResponse({'error': 'Invalid credentials'}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()


class ChefProfileViewSet(viewsets.ModelViewSet):
    queryset = ChefProfile.objects.all()
    serializer_class = ChefProfileSerializer
    permission_classes = [IsAuthenticated, IsChef]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAdmin]
        return super().get_permissions()



class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()



class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsChef]
        return super().get_permissions()



class FoodRateViewSet(viewsets.ModelViewSet):
    queryset = FoodRate.objects.all()
    serializer_class = FoodRateSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsUser]
        return super().get_permissions()

