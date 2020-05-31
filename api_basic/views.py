from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
