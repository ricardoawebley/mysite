from django.urls import path, include
from . import views

urlpatterns =[
    path('articles/', views.LatestArticlesList.as_view()),

]

