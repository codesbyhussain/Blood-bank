from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Donor, BloodGroup
from .forms import DonorForm, Eligible, appointment
from django.core.mail import send_mail, mail_admins
# Create your views here.
def index(request):
    return render(request, 'bldon/index.html')

def donorregister(request):
    if request.method == 'POST':
        form=DonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('appointment')

    else:
        form = DonorForm()

    return render(request, 'bldon/register.html', {'form':form})

def eligible (request):
    if request.method == 'POST':
        form1=Eligible(request.POST)
        if form1.is_valid():
            obj=form1.cleaned_data['donated']
            if obj == 'yes':
                return render(request,'bldon/donated.html')
            obj=form1.cleaned_data['age']
            if obj == 'no':
                return render(request,'bldon/age.html')
            obj=form1.cleaned_data['disease']
            if obj == 'yes':
                return render(request,'bldon/disease.html')

            return redirect('register')
    else:
        form1=Eligible()

    return render(request,'bldon/eligible.html', {'form1': form1})

def app(request):
    if request.method == 'POST':
        form=appointment(request.POST)
        if form.is_valid():
            obj=form.cleaned_data['setdate']
            donor=Donor.objects.last()
            email_val= getattr(donor, 'email')
            send_mail(donor, str(obj), 'avenger.hussain14@gmail.com', ['hussainjmanasi@gmail.com','albertjokelin@gmail.com','peterthomasbiju2001@gmail.com',email_val])
            return render(request, 'bldon/Emailsent.html')
    else:
        form=appointment()

    return render(request, 'bldon/appointment.html', {'form': form})
