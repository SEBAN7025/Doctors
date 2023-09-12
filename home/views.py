from django.shortcuts import render
from django.http import HttpResponse
from .models import departments,doctors

from .forms import bookingform

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')

    form = bookingform ()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctor(request):
    dict__docs={
        'doct': doctors.objects.all()
    }
    return render(request, 'doctors.html',dict__docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)

