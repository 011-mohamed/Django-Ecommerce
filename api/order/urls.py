
from django.urls import path

from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.ProductViewSet)


urlpatterns = [
    
    path('add/', views.addOrderItems, name="order-add"),
    path('', views.getOrders, name="order-list"),
    
]