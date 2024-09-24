from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request,'index.html')

def contact_view(request):
    if request.method == "POST":
            
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = f"From: {name} <{email}>\n\n{message}"
        send_mail(
          subject,
          full_message,
          settings.DEFAULT_FROM_EMAIL,
          [settings.DEFAULT_TO_EMAIL],
          fail_silently=False,  
        )
        email.send()
        
        return render(request,'index.html')

    return render(request,'index.html')