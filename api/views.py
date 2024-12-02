from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import FoodListSerializer
from food.models import Food, FoodCategory


class FoodCategoryListView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(is_publish=True)

        queryset = FoodCategory.objects.prefetch_related(
            Prefetch(
                "food",
                queryset=published_foods,
                to_attr="published_foods",
            )
        )

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
