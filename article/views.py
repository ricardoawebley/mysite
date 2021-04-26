from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class LatestArticlesList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()[0:4]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
