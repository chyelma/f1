from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from customuser.models import CustomUser,Counsellor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse, HttpResponseRedirect

# def register(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         Profession = request.POST['Profession']
#         Age = request.POST['Age']
#         phone_number= request.POST['phone_number']

#         if CustomUser.objects.filter(email=email).exists():
#             messages.info(request, 'email already exists!')
#             return redirect('register')
#         if len(password)<6:
#             messages.info(request, 'password must be of length 6 at least')
#             return redirect('register')
#         else:
#             user_obj = User.objects.create_user(email, email, password)
#             user_obj.save()
#             customuser = CustomUser.objects.create(user = user_obj , name=name,Profession=Profession,email=email,Age=Age,phone_number=phone_number)
#             customuser.save()
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        profession = request.POST['Profession']
        age = request.POST['Age']
        phone_number = request.POST['phone_number']

        # Check if the email contains allowed domains
        allowed_domains = ['@g.bracu.ac.bd', '@bracu.ac.bd']
        if not any(domain in email for domain in allowed_domains):
            messages.info(request, 'Registration is allowed only for @g.bracu.ac.bd or @bracu.ac.bd domains.')
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists!')
            return redirect('register')
        
        if len(password) < 6:
            messages.info(request, 'Password must be at least 6 characters long.')
            return redirect('register')
        else:
            user_obj = User.objects.create_user(email, email, password)
            user_obj.save()
            customuser = CustomUser.objects.create(user=user_obj, name=name, Profession=profession, email=email, Age=age, phone_number=phone_number)
            customuser.save()
            return redirect('login')

        
    else:
        return render(request,'register.html')
    
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('register')
        
        user = authenticate(username = email , password =password)
        if user is None:
            print("not working")
            messages.success(request, 'Wrong password.')
            return redirect('login')
        
        login(request , user)
        print('success')
        if user.is_superuser:
            return redirect('admin_dashboard')
        if Counsellor.objects.filter(email=email).exists():
            return redirect('counsellor_dashboard')
        if CustomUser.objects.filter(email=email).exists():
            return redirect('patient_dashboard')

    return render(request , 'login.html')
    

def logout_user(request):
    logout(request)
    print('logout success')
    return redirect('index')


@login_required
def patient_dashboard(request):
    return render(request,'patient_dashboard.html')

@login_required
def counsellor_dashboard(request):
    return render(request,'counsellor_dashboard.html')


def update_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        
        if new_password == confirm_password:
            user = User.objects.get(username=email)
            user.set_password(new_password) 
            user.save()
            return redirect('login')
        else:
            return HttpResponse("Passwords don't match!")
    else:
        return render(request, 'update_password.html')

def forgotpassword(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        user = CustomUser.objects.filter(phone_number=phone).first()
        if user:
            return render(request,'updatepassword.html')
    return render(request,'forgotpassword.html')


def aboutus(request):
    return render(request,'aboutus.html')