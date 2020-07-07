from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    pass