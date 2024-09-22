from rest_framework import serializers
from .models import CustomUser, ChefProfile, Ingredient, Food, FoodRate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']  

class ChefProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefProfile
        fields = '__all__' 

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True) 

    class Meta:
        model = Food
        fields = '__all__'

class FoodRateSerializer(serializers.ModelSerializer): 
    food = FoodSerializer(read_only=True)

    class Meta:
        model = FoodRate
        fields = '__all__'
