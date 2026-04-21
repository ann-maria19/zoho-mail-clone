def email_detail(request, email_id):
    # This looks for the specific email by its ID (primary key)
    email = Email.objects.get(id=email_id)
    
    # Mark it as read since the user is opening it!
    email.is_read = True
    email.save()
    
    return render(request, 'core/detail.html', {'email': email})