from django.contrib import admin
from django.urls import path, include # Add include here
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # This adds login/logout
    path('inbox/', views.inbox),
    path('send/', views.send_email),
    path('email/<int:email_id>/', views.email_detail, name='email_detail'),
    path('delete/<int:email_id>/', views.delete_email),
]