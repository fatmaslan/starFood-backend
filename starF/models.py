from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# class Meal(models.Model):
#     name=models.CharField(max_length=100)
#     price = models.IntegerField()
#     category = models.ForeignKey(Category,related_name='meals',on_delete=models.CASCADE)

class Food(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='meals', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class FoodImage(models.Model):
    food=models.ForeignKey(Food,related_name="images",on_delete=models.CASCADE)
    image=models.ImageField(upload_to="food_images/")

    def __str__(self):
        return f"Image of {self.food.title}"

