from multiprocessing import context
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from store.models import Category, Product
from django.contrib.auth.models import User
from comment.models import Comment

from .serializers import CategorySerializer, ProductSerializer, UserSerializer, CommentSerializer


def api_list(request):
    return render(request, 'store/api_list.html')


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CommentAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
