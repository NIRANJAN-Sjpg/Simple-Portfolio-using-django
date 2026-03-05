from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact   # ✅ Correct Import


def home(request):
    context = {'name': 'Niranjan', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ins = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        ins.save()

        print("Data has been saved to the database")

    return render(request, 'contact.html')
