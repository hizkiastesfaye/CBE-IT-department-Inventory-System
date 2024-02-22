from django.urls import path
from . import views

urlpatterns = [
    path('greet',views.greet,name='greet'),
    path('staff/dashboard',views.dashboard,name='dashboard_staff'),
    path('staff/items',views.item.as_view(),name='items_staff'),
    path('staff/checkout',views.checkoutView.as_view(),name='checkoutt_staff'),
    path('staff/request',views.Orders.as_view(),name='requests_staff'),
    path('staff/signup',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('staff/request_no',views.request_noView.as_view(),name='requests_no_staff'),
]