from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class: Inline admin descriptor for CarModel objects
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty CarModel objects displayed by default in the admin

# CarModelAdmin class: Custom admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'car_type', 'year']  # Fields to display in the admin list view
    list_filter = ['car_make', 'car_type', 'year']  # Add filters to the right sidebar
    search_fields = ['name', 'car_make__name']  # Enable search by car model name or car make name

# CarMakeAdmin class: Custom admin class for CarMake, with CarModel inline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']  # Fields to display in the admin list view
    search_fields = ['name']  # Enable search by car make name
    inlines = [CarModelInline]  # Attach the CarModel inline

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
