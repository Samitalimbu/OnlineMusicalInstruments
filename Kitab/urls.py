from unicodedata import name
from django.urls import path
from Kitab import views
from django.contrib.auth import views as auth_views
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

    path('viewbooking', views.viewbooking_view,name='viewbooking'),

    path('viewcustomer', views.viewcustomer, name='viewcustomer'),

    path('blog1', views.blog_detail, name='blog1'),

    path('blog2', views.blog_detail2, name='blog2'),

    path('blog3', views.blog_detail3, name='blog3'),

    path('blog4', views.blog_detail4, name='blog4'),

    path('profile/', views.profile, name='profile'),

    path('edit-profile/', views.edit_profile_view,name='edit-profile'),

    path('delete-product/<slug:p_id>',views.deleteproduct,name='delete-product'),

    path('Bdelete-product/<slug:p_id>',views.Bdeleteproduct,name='Bdelete-product'),


    path('update_product/<slug:id>',views.updateproduct),

    path('editproduct/<int:id>',views.editproduct),

   path("password_reset/", views.password_reset_request, name="password_reset"),

]




     



    



    
