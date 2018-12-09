from django.contrib import admin

# Register your models here.
from .models import Classification, MealTypes, NonSizableDishes, SizableDishes, Toppings	

admin.site.register(Toppings)
admin.site.register(Classification)
admin.site.register(MealTypes)
admin.site.register(NonSizableDishes)
admin.site.register(SizableDishes)

