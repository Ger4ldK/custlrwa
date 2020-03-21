from django.shortcuts import render
from rest_framework import viewsets, filters, generics, pagination
from .models import ScrapedCustomResult, ScrapedResult, Sizing, ImageUrl, Reviews
from .serializers import ScrapedResultSerializer, ScrapedCustomResultSerialzer, SizingSerializer, ImageListSerializer, ReviewsSerializer

class PaginationDefault (pagination.PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 120

class ResultPagination (pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 500

class ScrapedResultAPIView(generics.ListCreateAPIView):
    search_fields = ['product_name', 'brand', 'product_description', 'category', 'subcategory']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer
    pagination_class = ResultPagination
    http_method_names = ['get']

class ScrapedResultView(viewsets.ModelViewSet):
    queryset = ScrapedResult.objects.all()
    serializer_class = ScrapedResultSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class SizingAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Sizing.objects.all()
    serializer_class = SizingSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class ImageListAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = ImageUrl.objects.all()
    serializer_class = ImageListSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class ReviewsAPIView(generics.ListCreateAPIView):
    search_fields = ['=product__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = PaginationDefault
    http_method_names = ['get']

class ScrapedCustomResultView(viewsets.ModelViewSet):
    queryset = ScrapedCustomResult.objects.all()
    serializer_class = ScrapedCustomResultSerialzer
    http_method_names = ['get']