from django.urls import path
from . import views
from .views import order_detail_view

app_name = 'order'  # Defining the app namespace

urlpatterns = [
    # Order success page
    path('order-success/', views.order_success, name='order_success'),

    # All orders page
    path('all-orders/', views.all_orders, name='all_orders'),

    # Order details page
    # path('order-details/<int:order_id>/', views.order_details, name='order_details'),
    path('order/<int:serial_number>/', views.order_detail, name='order_detail'),

    # Cancel order page
    # path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order/cancel/<str:order_id>/', views.cancel_order, name='cancel_order'),









    path('order-management/', views.order_management, name='order_management'),

    path('admin-order/<int:order_serial_number>/', order_detail_view, name='order_detail_view'),

    path('change_order_status/<oid>/', views.change_order_status, name='change_order_status'),


]
