from django.urls import path

from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.ProductViewSet)


urlpatterns = [
    
    
    path('', views.getOrderItems, name="orderItem-list"),
    
]