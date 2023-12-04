"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', home),
    path('home', home),

    path('adminbooks', adminbooks_tab),
    path('readers', readers_tab),

    path('save', save_student),
    path('readers/add', save_reader),
    path('search_reader/', search_reader, name='search_reader'),

    path('books', books_tab),
    path('search_book/', search_books, name='search_books'),
    path('get_reader/', get_reader, name="get_reader"),
    
    path('add-to-bag/', views.add_to_bag, name="add-to-bag"), #to add to bag
    path('bag/', show_bag, name="showbag"), #to show bag
    path('checkout/', views.checkout.as_view(), name="checkout"),

    path('removebag/', views.remove_bag), #to remove from bag
    path('showbag', views.show_bag), #to show bag
    path('plusbaglist/', views.add_to_bag), #to Add to Bag
    path('minusbaglist/', views.remove_bag), #to Added to Bag
    path('pluswishlist/', views.plus_wishlist), #to Green Button
    path('minuswishlist/', views.minus_wishlist), #to Red Button
    path('wishlist/', views.show_wishlist, name='showwishlist'),

    path('mybag', mybag_tab),
    #path('search/', reader_search, name="reader_search"),
    path('returns', returns_tab),
    path('orders', views.orders, name="orders"),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    #login authentication
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),

    #password change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html', form_class=MyPasswordChangeForm, success_url='/password_changedone'), name='password_change'),
    path('password_changedone/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    #logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Library Management System - UOM"
admin.site.site_title = "Library Management System - UOM"
admin.site.site_index_title = "Welcome to Library Management System - UOM"
