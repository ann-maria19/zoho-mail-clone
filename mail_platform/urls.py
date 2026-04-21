from django.contrib import admin
from django.urls import path
from core import views  # Importing our views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inbox/', views.inbox),
    path('send/', views.send_email), 
    path('email/<int:email_id>/', views.email_detail, name='email_detail'),
]