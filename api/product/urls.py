from unicodedata import name
from rest_framework import routers
from django.urls import path, include


from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.ProductViewSet)


urlpatterns = [
    path('', views.getProducts, name='products'),
    path('<str:pk>/', views.getProduct, name="product-detail"),
    
    path('getProductWithLowqty', views.getProductWithLowQty, name="product-With-lowQty"),
    path('getProductByRef/<str:sampleId>', views.getProductByRef, name="product-detail"),
    path('orderByDate', views.getProductsOrderByDate, name="product-list-ordered"),
    path('search/<str:keyword>', views.getProductsFiltred, name='products-filter'),
    path('delete/<str:pk>', views.deleteProduct, name="product-delete"),
    path('update/<str:ck>', views.updateProduct, name="product-update"),
    path('add', views.addProduct, name="product-add"),
    path('findByCategory/<str:ck>/', views.getProductByCategory, name='product-category'),
    path('count', views.getCountOfProducts, name="product-count"),
    
];