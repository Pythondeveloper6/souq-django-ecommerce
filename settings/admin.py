from django.contrib import admin

# Register your models here.
from .models import Brand , Variant

admin.site.register(Brand)
admin.site.register(Variant)