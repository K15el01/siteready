"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from xml.dom.minidom import Document
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация  ',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('links/', views.links, name='links'),
    path('anketa/', views.anketa, name='anketa'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/',views.newpost, name='newpost'),
    path('videopost/',views.videopost, name='videopost'),
    path('registration/', views. registration, name= 'registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('products/', views.product_list, name='products_list'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('orders/', views.all_orders, name='all_orders'),
    path('orders/<int:order_id>/update_status/', views.update_order_status, name='update_order_status'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
