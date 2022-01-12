from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'POST':
        pass
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')
