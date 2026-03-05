from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'form.html')

def about(request):
    return render(request, 'about.html')

def form_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        age = request.POST.get('age', '')
        if fullname and age:
            return redirect('about')
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ</h1>")
