from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Email Folders
    path('inbox/', views.inbox),
    path('sent/', views.sent_emails),
    path('trash/', views.trash_emails), # Added this for you
    
    # Email Actions
    path('send/', views.send_email),
    path('email/<int:email_id>/', views.email_detail, name='email_detail'),
    path('delete/<int:email_id>/', views.delete_email),
    
    # Optional: Redirect the empty home page to the inbox
    path('', views.inbox), 
]