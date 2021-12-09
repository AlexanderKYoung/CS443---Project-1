from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='storefront-home'),
    path('register/', views.register, name='register'),
    path('point-of-sale/', views.pos, name="point-of-sale"),
    path('tickets/', views.tickets, name="tickets"),
    path('search-customers/', views.customer_search_view, name="customer-search"),
    path('make-order/', views.order, name="make-order"),
    path('orders/', views.orders, name="orders"),
    path('inventory/', views.stocks, name="stocks"),
    path('list-stock/', views.StockListView.as_view(), name="list-stock"),
    path('customer/new/', views.CustomerCreateView.as_view(), name="customer-create"),
    path('stock/new/', views.StockCreateView.as_view(), name="stock-create")
]