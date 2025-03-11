from django.urls import path
from .views import *

urlpatterns = [
    path('wishes/',Wishes,name='wishes'),
    path('wishes2/',Wishes2,name='wishes2'),
    path('std_name/<str:a>',std_name,name='std_name'),
    path('std_age/<int:b>',std_age,name='std_age'),
    path('Base_html/',Base_html,name='Base_html'),
    path('static/',static,name='static'),
    path('page_redirection_home/',page_redirection_home,name='page_redirection_home'),
    path('about/',page_redirection_about,name='page_redirection_about'),
    path('contact/',page_redirection_contact,name='page_redirection_contact'),
    path('home/',extends_home,name='extends_home'),
    path('extends_about/',extends_about,name='extends_about'),
    path('extends_contact/',extends_contact,name='extends_contact'),
    path('datatohtml/',datatohtml,name='datatohtml'),
    path('ormqueries/',ormqueries,name='ormqueries'),
    path('ormqueries2/',ormqueries2,name='ormqueries2'),
    path('',register,name='register'),
    path('login/',login,name='login'),
    path('list/',student_list,name='student_list'),
    path('student_order/',student_order,name='student_order'),
    path('student_count/',student_count,name='student_count'),
    path('filter/',student_filter,name='student_filter'),
    path('filter_update/',student_filter_update,name='student_filter_update'),
    path('filter_delete/',student_filter_delete,name='student_filter_delete'),
]