from django.urls import path
from api import views

urlpatterns = [
    path('', views.index),
    # path('reviews/', views.allreviews),
    path('login/', views.login)
]
