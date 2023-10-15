from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, pagination, serializers
from .serializers import ArticleSerializer
from rest_framework import filters
from .models import Article
from rest_framework.exceptions import ValidationError
from django.shortcuts import render


# Create your views here.


# Create a custom pagination class if needed
class PagePagination(pagination.PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class AllArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by("?")
    serializer_class = ArticleSerializer
    pagination_class = PagePagination
    categories = [
        "world",
        "sport",
        "business",
        "science_and_technology",
        "education",
        "entertainment",
        "health",
        "travel"
    ]
    countries = [
        'us',
        'gb',
        'ng',
        'eg',
        'sa',
        'ae',
        'ca',
        'mx',
        'it',
        'de',
        'ar',
        'es',
        'jp',
        'au',
        'fr',
        'be',
        'tr',
        'ua',
        'ru',
        'br',
        'id',
        'in',
    ]

    def get_queryset(self):
        country_code = self.request.query_params.get('country_code')
        category = self.request.query_params.get('category')
        page_size = self.request.query_params.get('page_size')
        page = self.request.query_params.get('page')
        queryset = self.queryset

        if country_code and country_code not in self.countries:

            raise ValidationError(
                {'detail': 'Invalid country_code'}
            )

        if category and category not in self.categories:

            raise ValidationError(
                {'detail': 'Invalid category'}
            )

        if not any([country_code, category, page_size, page]):
            queryset = queryset.all()

        if country_code:
            queryset = queryset.filter(country_code=country_code)

        if category:
            queryset = queryset.filter(category=category)

        if page_size:
            try:
                # Update the page size in the pagination class
                if int(page_size) <= 0:
                    self.pagination_class.page_size = 10
                else:
                    self.pagination_class.page_size = int(page_size)

            except:
                self.pagination_class.page_size = 10

        return queryset


def docs_view(request):
    return render(request, "news/docs.html")


def dev_view(request):
    return render(request, "news/developer.html")
