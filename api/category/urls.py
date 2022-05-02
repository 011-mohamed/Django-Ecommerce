from rest_framework import routers
from django.urls import path, include

from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.CategoryViewSet)

urlpatterns = [
    path('', views.getCategory , name='category'),
    path('<str:pk>/', views.getCat, name="cat"),
    
    path('create/', views.createCategory, name="category-create "),
    path('delete/<str:pk>', views.deleteCategory, name="category-delete"),
    path('update/<str:pk>', views.updateCategory, name="category-updated"),
    
]