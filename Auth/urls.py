from Auth import views
from django.urls import path




app_name = "Auth"

urlpatterns = [
    
    # path('home/', views.HomePostView.as_view()),
    path('sign_up/', views.SignUp.as_view()),
   
]