from django.urls import path
from user import views


urlpatterns = [
     
    path('login/',views.loginFun,name='login'),
    path('registration/',views.registrationFun,name='registration'),
    path('logout/',views.logoutFun,name='logout'),
]