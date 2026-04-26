from django.shortcuts import render, redirect, get_object_or_404
from .models import Email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def inbox(request):
    # Only show emails sent TO the logged-in user that aren't deleted
    emails = Email.objects.filter(recipient_email=request.user, is_deleted=False).order_by('-timestamp')
    return render(request, 'inbox.html', {'emails': emails, 'folder': 'inbox'})

@login_required
def sent_emails(request):
    # Only show emails sent BY the logged-in user
    emails = Email.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'emails': emails, 'folder': 'sent'})

@login_required
def trash_emails(request):
    # Show emails the user received but marked as deleted
    emails = Email.objects.filter(recipient_email=request.user, is_deleted=True).order_by('-timestamp')
    return render(request, 'inbox.html', {'emails': emails, 'folder': 'trash'})

@login_required
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id)
    
    # Security check: Only allow the sender or actual recipient to see the email
    if request.user == email.sender or request.user == email.recipient_email:
        email.is_read = True
        email.save()
        return render(request, 'detail.html', {'email': email})
    
    return redirect('/inbox/')

@login_required
def send_email(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        
        try:
            # Look up the User object based on the username typed in the form
            recipient_user = User.objects.get(username=recipient_username)
            Email.objects.create(
                sender=request.user,
                recipient_email=recipient_user, 
                subject=subject,
                body=body
            )
            return redirect('/inbox/')
        except User.DoesNotExist:
            # If the username doesn't exist, reload with an error message
            return render(request, 'send_email.html', {'error': 'User not found!'})
            
    return render(request, 'send_email.html')

@login_required
def delete_email(request, email_id):
    # Ensure only the recipient can delete the email from their view
    email = get_object_or_404(Email, id=email_id, recipient_email=request.user)
    email.is_deleted = True
    email.save()
    return redirect('/inbox/')