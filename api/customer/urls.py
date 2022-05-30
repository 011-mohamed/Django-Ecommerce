from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCustomers, name='customers'),
    path('filtred/<str:tel>', views.getCustomersByPhoneNumber, name='customer-filtred'),
    path('search/<str:keyword>', views.getCustomersFiltredByName, name='Customers-filtred-Name'),
    path('searchByTel/<str:keyword>', views.getCustomersFiltredByPhoneNumber, name='Customers-filtred-Name'),
    path('orderByDate', views.getCustomersOrderByDate, name='Customers-ordered'),
    
    
    path('update/<str:pk>', views.updateCustomer, name="customer-updated"),
    path('create/', views.createCustomer, name="customer-create "),
    path('delete/<str:pk>', views.deleteCustomer, name="customer-delete"),
    path('<str:pk>/', views.getCustomer, name="customer"),
    path('customersCount', views.getCountOfCustomers, name="customer-count "),
]