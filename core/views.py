from django.shortcuts import render, redirect, get_object_or_404
from .models import Email
from django.contrib.auth.models import User

def inbox(request):
    folder = request.GET.get('folder', 'inbox')
    
    if folder == 'sent':
        # Shows mail where the first user is the sender
        emails = Email.objects.filter(sender=User.objects.first(), is_deleted=False).order_by('-timestamp')
    elif folder == 'trash':
        emails = Email.objects.filter(is_deleted=True).order_by('-timestamp')
    else:
        # Default inbox logic
        emails = Email.objects.filter(is_deleted=False).order_by('-timestamp')

    return render(request, 'core/inbox.html', {'emails': emails, 'folder': folder})

def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    email.is_read = True
    email.save()
    return render(request, 'core/detail.html', {'email': email})

def send_email(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        
        # Create the email in the database
        Email.objects.create(
            sender=User.objects.first(),
            recipient_email=recipient,
            subject=subject,
            body=body
        )
    return redirect('/inbox/')

def delete_email(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    email.is_deleted = True
    email.save()
    return redirect('/inbox/')