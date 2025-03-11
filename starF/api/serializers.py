from rest_framework import serializers
from starF.models import Food,Category,FoodImage


# class MealSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Meal
#         fields='__all__'

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ['id','image']

class FoodSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True,read_only=True)
    class Meta:
        model = Food
        fields = ['id', 'title', 'description', 'price', 'category', 'images']

class CategorySerializer(serializers.ModelSerializer):
    meals=FoodSerializer(many=True,read_only=True)
    foods = FoodSerializer(many=True, read_only=True, source="food_set")
    class Meta:
        model = Category
        fields='__all__'










