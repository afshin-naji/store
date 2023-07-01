from django.urls import path
from .views import api_list, CategoryAPIView, ProductAPIView, UserAPIView, CommentAPIView


urlpatterns = [
    path('', api_list, name='api_list'),
    path('categories/', CategoryAPIView.as_view(), name='api_categories'),
    path('products/', ProductAPIView.as_view(), name='api_products'),
    path('users/', UserAPIView.as_view(), name='api_users'),
    path('comments/', CommentAPIView.as_view(), name='api_comments'),
]