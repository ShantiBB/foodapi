from django.urls import path

from api.views import FoodCategoryListView

urlpatterns = [
    path("foods/", FoodCategoryListView.as_view(), name="food_category_list"),
]
