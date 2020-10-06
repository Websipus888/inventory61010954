from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('about',views.about,name='about'),
    path('contract',views.contract,name='contract'),
    path('random',views.random,name='random'),
    path('signup',views.signup,name='signup'),
]
