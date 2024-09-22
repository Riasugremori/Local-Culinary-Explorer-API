from django.contrib import admin
from .models import CustomUser, ChefProfile, Ingredient, Food, FoodRate
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}), 
    )


class ChefProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialty']
    search_fields = ['user__username', 'specialty']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['description']
    filter_horizontal = ('ingredients',) 
    search_fields = ['description']


class FoodRateAdmin(admin.ModelAdmin):
    list_display = ['food', 'rate']
    search_fields = ['food__description']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ChefProfile, ChefProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodRate, FoodRateAdmin)
