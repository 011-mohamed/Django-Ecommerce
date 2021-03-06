from api.invoice import views
from rest_framework import routers
from django.urls import path, include

from . import views

#router = routers.DefaultRouter()
#router.register(r'', views.CategoryViewSet)

urlpatterns = [
    
    path('', views.getBills, name="invoice-list"),
    path('order', views.getBillsOrderByDate, name="invoice-list-order"),
    path('create/', views.addBill, name="invoice-create"),
    path('search/<str:keyword>', views.getBillssFiltredByName, name='invoice-filtred-Name'),
    path('searchByPhone/<str:keyword>', views.getBillssFiltredByPhoneNumber, name='products-filter-PhoneNumber'),
    path('billsCount', views.getCountOfBills, name="invoice-count"),
    path('sumPerMonth', views.sumOfBills, name="invoice-sum"),
]