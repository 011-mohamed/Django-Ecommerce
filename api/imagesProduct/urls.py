from django.urls import path
from . import views


urlpatterns = [
    path('', views.getImagesProduct, name='images-product'),
    path('findByProduct/<str:ck>/', views.getImagesProductById, name='images-product-filtred'),
    path('findByReference/<str:ref>/', views.getIdProductByRef, name='product-by-ref')
]