from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('users/', views.UserList.as_view()),
    path('reviews/', views.AllReviews.as_view()),
    path('review/', views.OwnReview.as_view(), name="review"),
    path('review/<int:pk>/', views.ReviewInfo.as_view(), name="review_info"),
    path('company/', views.AllCompany.as_view(), name="company"),
    path('company/<int:pk>/', views.CompanyInfo.as_view(), name="company_detail"),
]
