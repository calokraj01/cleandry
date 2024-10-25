from django.shortcuts import render
from datetime import datetime
from apps.models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, phone=phone, message=message, date =datetime.today())
        contact.save()

    return render(request, 'index.html')