from django.urls import path
from .views import admin_login,logout_admin,admin_dashboard,enroll_counsellor,cancel_appointment
urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', logout_admin, name='admin_logout'),
    path('enroll-counsellor/', enroll_counsellor, name='enroll_counsellor'),
    path('cancel_appointment/<int:pk>/', cancel_appointment, name='cancel_appointment'),
]