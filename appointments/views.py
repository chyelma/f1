from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Appointment,AppointmentRequest
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from customuser.models import CustomUser,Counsellor####
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Document
from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.
@login_required
def create_appointment(request):
    if request.method == 'POST':
        councellor_name = request.POST['councellor_name']
        a_date = request.POST['a_date']
        a_time = request.POST['a_time']
        councellor_email = request.user.username
        creator = Counsellor.objects.get(email=councellor_email)

        
        appointment= Appointment(
            councellor_name=councellor_name,
            councellor_email=councellor_email,
            a_date=a_date,
            a_time=a_time,
            user=creator
            )
        
        appointment.save()
        return HttpResponse('Appointment Created')
    else:
        return render(request, 'create_appointment.html')
    
@login_required
def req_appointment(request,pk):

    email = request.user.username
    creator = CustomUser.objects.get(email=email)
    appointment=Appointment.objects.get(pk=pk)
    posted_by=appointment.councellor_name

    if request.method == 'POST':
        reason = request.POST['reason']
        mobile = request.POST['mobile']
        requester_email = request.POST['requester_email']

        
        appointment_request= AppointmentRequest(
            requested_by=creator,
            appointment=appointment,
            posted_by=posted_by,
            reason=reason,
            mobile=mobile,
            email=requester_email,
            approved=False)
        print(appointment_request)
        
        appointment_request.save()
            
        HttpResponse("Successfully requested!")
    
    context={'appointment':appointment}
    
    return render(request, 'make_appointment_request.html',context)

def view_all_appointment(request):
    appointments = Appointment.objects.filter(approved=False)
    context={'appointments':appointments,'user':request.user}
    return render(request, 'view_all_appointment.html', context)

def upcoming_appointment(request):
    current_user_email = request.user.email
    
    filtered_data = AppointmentRequest.objects.filter(requested_by_id=current_user_email)

    return render(request, 'upcoming_appointment.html', {'filtered_data': filtered_data})

def cancel_appointment(request,pk):
    print(pk)
    return render(request, 'upcoming_appointment.html')

#########Shafiul 

def videocall(request):
    current_user_email = request.user.email

    filtered_data = AppointmentRequest.objects.filter(requested_by_id=current_user_email)

    return render(request, 'videocall.html', {'filtered_data': filtered_data})
 
def index(request):
    return render(request,'index.html')



def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})


from django.shortcuts import render

def upload_success(request):
    return render(request, 'upload_success.html')  


 

def view_uploaded_documents(request):
    documents = Document.objects.all()  
    return render(request, 'view_documents.html', {'documents': documents})


from .forms import StoryForm

def story_upload(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story_page')  
    else:
        form = StoryForm()
    
    return render(request, 'story_upload.html', {'form': form})


from .models import PatientStory

def story_page(request):
    stories = PatientStory.objects.all().order_by('-uploaded_at') 
    return render(request, 'story_page.html', {'stories': stories})

