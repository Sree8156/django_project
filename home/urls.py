from .import views
from django.urls import path
from .views import add_to_cart

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginn,name="login"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('phone',views.phone,name="phone"),
    path('pad',views.pad,name="pad"),
    path('mac',views.mac,name="mac"),
    path('accessories',views.accessories,name="accessories"),
    path('cart',views.add_to_cart,name="cart"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

]