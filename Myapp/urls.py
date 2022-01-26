from django.urls import path, include
from Myapp import views

urlpatterns = [
    path('',views.Product,name='Product'),
    path('order',views.Order,name='order'),
    path('webdata',views.WebData,name="webdata")
]