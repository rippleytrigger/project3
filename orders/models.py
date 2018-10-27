from django.db import models

# Create your models here.
class Classification(models.Model):
    title = models.CharField(max_length=120)

    def _str_(self):
        return f"{self.title}"

class mealTypes(models.Model):
    title = models.CharField(max_length=120) 

    def _str_(self):
        return f"{self.title}"

class Modifiers(models.Model):
    title = models.CharField(max_length=120) 

    def _str_(self):
        return f"{self.title}"

class dishes():
    title = models.CharField(max_length=120)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    sizable = models.BooleanField()
    price_1 = models.FloatField(null=True, blank=True, default=0)
    price_2 = models.FloatField(null=True, blank=True, default=0)
    meal_type =  models.ForeignKey(mealTypes, on_delete=models.CASCADE)


class OrderAdditions(models.Model):
    dish = models.ForeignKey(dishes, on_delete=models.CASCADE)
    additions = models.ForeignKey(Modifiers, on_delete=models.CASCADE)


"""
class NonSizableDishes(models.Model):
    title = models.CharField(max_length=120)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    meal_type =  models.ForeignKey(mealTypes, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.title} / {self.classification}"

class SizableDishes(models.Model):
    title = models.CharField(max_length=120)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    price_small = models.FloatField(null=True, blank=True, default=0)
    price_large = models.FloatField(null=True, blank=True, default=0)
    meal_type =  models.ForeignKey(mealTypes, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.title} / {self.classification}"
"""     

class MenuOrders(models.Model): 
    dish = models.ForeignKey(mealTypes, on_delete=models.CASCADE)
    has_additions = models.BooleanField()
    additions = models.ManyToManyField(OrderAdditions)

    def _str_(self):
        return f"{self.title}"