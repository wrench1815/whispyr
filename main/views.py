from django.shortcuts import redirect, render
from .models import SecretMessage
# Create your views here.


def home(request):
    if request.method == 'POST':
        message = request.POST['SecetMessage']

        SecretMessage.objects.create(message=message)
        return redirect('/')

    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')
