from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getCustomers, name='customers'),
    path('filtred/<str:tel>', views.getCustomersByPhoneNumber, name='customers-filtred'),

     path('update/<str:pk>', views.updateCustomer, name="customer-updated"),

    path('create/', views.createCustomer, name="customer-create "),
   
    path('delete/<str:pk>', views.deleteCustomer, name="customer-delete"),
    path('<str:pk>/', views.getCustomer, name="customer"),
]