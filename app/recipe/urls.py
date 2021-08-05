from django.conf.urls import url
from django.urls import path,include
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('views', views.TagViewSet)
router.register('ingredients', views.IngViewset)
router.register('recipes',views.RecipeViewset)

app_name = "recipe"
urlpatterns = [
    path('',include(router.urls)),
    path('ingredients',views.IngViewset),
    path('tag',views.TagViewSet),
    
    
]

