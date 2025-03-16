from django.urls import path
from .views import *

urlpatterns = [
    path('user_input/',user_input,name='user_input'),
    path('Profile/',Profile,name='Profile'),
    path('Profile_2/',Profile_2,name='Profile_2'),
    path('homepage/',homepage,name='homepage'),
    path('authregister/',authregister,name='authregister'),
    path('authlogin/',authlogin,name='authlogin'),
    path('authlogout/',authlogout,name='authlogout'),
    path('add_book/',add_book,name='add_book'),
    path('book_list/',book_list,name='book_list'),
]