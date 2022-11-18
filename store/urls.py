from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
<<<<<<< HEAD
=======
    path('process_order/', views.processOrder, name="process_order"),
>>>>>>> c637ee1 (Some Updating Fitures)
]