from django.contrib import admin
from .models import Food, FoodCategory


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "name_en", "name_ch", "order_id")
    search_fields = ("name_ru", "name_en", "name_ch")
    list_filter = ("order_id",)


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "name_ru",
        "internal_code",
        "category",
        "cost",
        "is_publish",
    )
    search_fields = ("name_ru",)
    list_filter = ("category", "is_publish")


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
