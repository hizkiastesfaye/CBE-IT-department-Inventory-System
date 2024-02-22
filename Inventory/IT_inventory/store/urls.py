from django.urls import path
from . import views

urlpatterns = [
    path('dashboar',views.dashboardView.as_view(),name='dashboard_store'),
    path('checkout',views.Checkoutview.as_view(),name='checkoutt_store'),
   
]