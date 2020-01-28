from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
    path('reviews/', views.AllReviews.as_view()),
    path('review/', views.OwnReview.as_view()),
    path('review/<int:pk>/', views.ReviewInfo.as_view()),
    path('company/', views.AllCompany.as_view()),
    path('company/<int:pk>/', views.CompanyInfo.as_view()),

]
