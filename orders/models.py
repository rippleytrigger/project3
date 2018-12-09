from django.db import models

# Create your models here.
class Classification(models.Model):
    title = models.CharField(max_length=120)

    def __str__ (self):
        return f"{self.title}"

class MealTypes(models.Model):
    title = models.CharField(max_length=120) 

    def __str__ (self):
        return f"{self.title}"

class Toppings(models.Model):
    title = models.CharField(max_length=120) 

    def __str__ (self):
        return f"{self.title}"

class NonSizableDishes(models.Model):
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    meal_type =  models.ForeignKey(MealTypes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.classification} {self.name}"

class SizableDishes(models.Model):
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price_small = models.FloatField(null=True, blank=True, default=0)
    price_large = models.FloatField(null=True, blank=True, default=0)
    meal_type =  models.ForeignKey(MealTypes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.classification} {self.name}"
"""
class MenuOrders(models.Model): 
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    has_additions = models.BooleanField()
    additions = models.ManyToManyField(Additions)

    def _str_(self):
      return f"{self.title}"
 """ 
"""
class Dishes(models.Model):
    title = models.CharField(max_length=120)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    sizable = models.BooleanField()
    price_1 = models.FloatField(null=True, blank=True, default=0)
    price_2 = models.FloatField(null=True, blank=True, default=0)
    meal_type =  models.ForeignKey(MealTypes, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.classification} {self.title}"
"""

"""
class OrderAdditions(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    additions = models.ForeignKey(Additions, on_delete=models.CASCADE)
"""


"""
class MenuOrders(models.Model): 
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    has_additions = models.BooleanField()
    additions = models.ManyToManyField(Additions)

    def _str_(self):
        return f"{self.title}"
"""





