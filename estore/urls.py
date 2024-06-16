# estore/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLoginView

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    # path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('', CustomLoginView.as_view(), name='login'),
    path('products/<int:product_id>/add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
]
