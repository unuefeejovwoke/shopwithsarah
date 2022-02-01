from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('ownshop/', views.own_shop, name='own_shop'),
    path('shop_admin/', views.shop_admin, name='shop_admin'),

    path('add-product/', views.add_product, name='add_product'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]
