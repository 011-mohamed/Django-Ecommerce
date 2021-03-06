import imp
from unicodedata import name
from django.urls import path , include 
from rest_framework import views
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home , name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('order/', include('api.order.urls')),
    path('orderItem/', include('api.orderItem.urls')),
    path('customers/', include('api.customer.urls')),
    path('bills/', include('api.invoice.urls')),
    path('imagesProduct/', include('api.imagesProduct.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

                         