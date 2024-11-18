from django.shortcuts import render, redirect

from myApp.models import Appointment, Contact
from myApp.forms import AppointmentForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def myservice(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method == 'POST':
        myappointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointment.save()
        return redirect('appointment')

    else:
        return render(request, 'appointment.html')


def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('contact')
    else:
        return render(request, 'contact.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointment': allappointments})

def delete(request, id):
    appoint =  Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def showcontact(request):
    allcontacts = Contact.objects.all()
    return render(request, 'showcontact.html', {"contacts": allcontacts})

def deletecontact(request, id):
    selectedcontact = Contact.objects.get(id=id)
    selectedcontact.delete()
    return redirect('/showcontact')

def edit(request, id):
    editappointments = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {"appointment": editappointments})

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')
