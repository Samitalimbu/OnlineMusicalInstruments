from unicodedata import name
from django.urls import path
from Kitab import views
from django.contrib import admin
from django.contrib import admin

from django.contrib.auth.views import LoginView





urlpatterns = [
    path('', views.home, name='home'),


     path('aboutus', views.aboutus, name='aboutus'),



     path("login/",views.login,name="login"),
     path("register/", views.register,name="register"),
    

    path('contact', views.contact,name='contact'),


    path("adminlogin/",views.adminlogin,name="adminlogin"),


    path('dashboard', views.dashboard,name='dashboard'),



    path('logout', views.logout, name="logout"),



    # Most important functon
    path('afterlogin', views.afterlogin_view, name="afterlogin"),


    path('admindashboard',views.admindashboard_view, name="admindashboard"),

    path('addData', views.Kitab,name='addData'),


    path('buyNow/<int:p_id>', views.buyNow,name='buyNow'),




    path('book_details/<int:p_id>', views.book_details,name='book_details'),


    path('admin-products', views.admin_products_view,name='admin-products'),

    path('addproduct', views.admin_add_product_view, name='addproduct'),
]


     



    



    
