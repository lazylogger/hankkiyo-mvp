from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Heidi SQL 에서 insert 쿼리문 돌려서 데이터 삽입했더니 장고 admin 사이트에선 그 데이터를 읽을 수 없었음.
    아래 코드를 추가하여 가능하게 됨.
    """
    def save_model(self, request, obj, form, change):
        super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super(StoreAdmin, self).save_model(request, obj, form, change)


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super(MenuAdmin, self).save_model(request, obj, form, change)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
