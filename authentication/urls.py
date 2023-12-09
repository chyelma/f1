from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name = 'register'),
    path('auth',views.register, name = 'auth'),
    path('login/',views.login_user, name= 'login'),
    path('logout/',views.logout_user, name= 'logout'),
    path('forgotpassword/',views.forgotpassword, name= 'forgotpassword'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('update_password/', views.update_password, name='update_password'),
    path('counsellor_dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),
]