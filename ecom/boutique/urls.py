from django.urls import path
from . import views

app_name = 'boutique'

urlpatterns = [
    #path('', views.product_list, name='product_list'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('', views.main, name='main'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('product/', views.product_list, name='product_list'),
    path('checkout/', views.checkout, name='checkout'),


]