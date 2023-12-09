from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
#from appointments.models import 
from customuser.models import CustomUser,Counsellor
from appointments.models import AppointmentRequest 
from django.utils import timezone

def admin_login(request):
    try:
        if request.user.is_authenticated and request.user.is_stuff:
            return redirect('admin_dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj= User.objects.filter(username=username)
            if not user_obj.exists():
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj=authenticate(username=username,password=password)

            if user_obj and user_obj.is_staff:
                login(request,user_obj)
                return redirect('admin_dashboard')
            else:
                return redirect('/')
        
        return render(request,'admin_login.html')
    
    except Exception:
        return redirect('index')
    
def logout_admin(request):
    logout(request)
    print('logout success')
    return redirect('admin_login')

@staff_member_required(login_url = reverse_lazy('admin_login'))
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

@staff_member_required(login_url = reverse_lazy('admin_login'))
def enroll_counsellor(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        phone_number= request.POST['phone_number']

        if Counsellor.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('enroll_counsellor')
        if len(password)<6:
            messages.info(request, 'password must be of length 6 at least')
            return redirect('enroll_counsellor')
        else:
            user_obj = User.objects.create_user(email, email, password)
            user_obj.save()
            counsellor = Counsellor.objects.create(user = user_obj , name=name,email=email,phone_number=phone_number,gender=gender)
            counsellor.save()
            print('counsellor created')
            return redirect('admin_dashboard')
        
    else:
        return render(request,'register.html')


def cancel_appointment(request,pk):
    appointment = AppointmentRequest.objects.filter(id=pk) # Get the specific appointment
    appointment.delete()  # Delete the appointment
    return render(request, 'upcoming_appointment.html')
