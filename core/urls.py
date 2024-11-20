from . import views
from django.urls import path

urlpatterns = [

    path('register/' , views.UserRegisterView.as_view() , name= 'user_register'),   
    path('token/' , views.UserLoginView.as_view() , name= 'user_login'),   
    path('token/logout/' , views.UserLogoutView.as_view() , name= 'user_logout'),   

]