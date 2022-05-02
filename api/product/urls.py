from unicodedata import name
from rest_framework import routers
from django.urls import path, include

from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.ProductViewSet)


urlpatterns = [
    path('', views.getProducts, name='products'),
    path('<str:pk>/', views.getProduct, name="product-detail"),
    
    path('search/<str:keyword>', views.getProductsFiltred, name='products-filter'),
    path('delete/<str:pk>', views.deleteProduct, name="product-delete"),
    path('update/<str:ck>', views.updateProduct, name="product-update"),
    
    path('findByCategory/<str:ck>/', views.getProductByCategory, name='product-category'),
    
]