from rest_framework import viewsets
from starF.models import Food,Category,FoodImage
from .serializers import CategorySerializer, FoodSerializer,FoodImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import RetrieveAPIView


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer


    @action(detail=False, methods=['get'], url_path=r'category/(?P<category_id>\d+)')
    def foods_by_category(self,request,category_id=None):
        foods = Food.objects.filter(category_id=category_id)
        serializer=self.get_serializer(foods,many=True)
        return Response(serializer.data)
    
    
    @action(detail=True,methods=['get'],url_path=r'(?P<food_id>\d+)')
    def food_detail(self, request, food_id=None):
        food = Food.objects.get(id=food_id)
        serializer = self.get_serializer(food)
        return Response(serializer.data)

class FoodImageViewSet(viewsets.ModelViewSet):
    queryset =FoodImage.objects.all()
    serializer_class = FoodImageSerializer
    parser_classes = [MultiPartParser,FormParser]