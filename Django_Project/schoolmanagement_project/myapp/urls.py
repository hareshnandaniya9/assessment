from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('feedback/',views.feedback,name="feedback"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    # path('change_password/',views.change_password,name="change_password"),
    path('help/',views.help,name="help"),
    path('terms/',views.terms,name="terms"),
    path('contect/',views.contect,name="contect"),
    path('change_password/',views.change_password,name="change_password"),
    path('forget_password/',views.forget_password,name="forget_password"),
    path('verify_otp/',views.verify_otp,name="verify_otp"),
    path('update_password/',views.update_password,name="update_password"),
    path('Profile/',views.Profile,name="Profile"),
    
   
]
