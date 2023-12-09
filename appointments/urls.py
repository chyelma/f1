from django.urls import path
from .views import create_appointment,req_appointment,view_all_appointment,upcoming_appointment,videocall,index,upload_document,upload_success,view_uploaded_documents,story_upload,story_page

urlpatterns = [
    path('create_appointment/', create_appointment , name='create_appointment'),
    path('upcoming_appointment/', upcoming_appointment, name='upcoming_appointment'),
    path('view_all_appointment/', view_all_appointment, name='view_all_appointment'),
    path('<int:pk>/request_appointment/', req_appointment, name='request_appointment'), 
    path('meeting/',videocall, name='meeting'), 
    path('index/',index, name='index'),
    path('upload/',upload_document, name='upload_document'),
    path('upload/success/', upload_success, name='upload_success'),
    path('documents/', view_uploaded_documents, name='view_documents'),
    path('upload_story/',story_upload, name='story_upload'),
    path('story_page/',story_page, name='story_page'),
    
]


from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)