from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import PatientRegistration
from .models import User

# Create your views here.

#Add new items and show new items
def add_show(request):
    pr = PatientRegistration(request.POST)
    if request.method == 'POST':
        pr = PatientRegistration(request.POST)
       # detail = User.objects.all()
        if pr.is_valid():

            fn = pr.cleaned_data['First_name']
            ln = pr.cleaned_data['Last_name']
            ge = pr.cleaned_data['Gender']
            ag = pr.cleaned_data['Age']
            di = pr.cleaned_data['Disease']
            dn = pr.cleaned_data['Doctor_name']
            df = pr.cleaned_data['Doctor_fees']
            md = pr.cleaned_data['Med_date']
            reg = User(First_name=fn, Last_name=ln, Gender=ge, Age=ag, Disease=di, Doctor_name=dn, Doctor_fees=df, Med_date=md)
            reg.save()
            pr = PatientRegistration()
            

    else:
        pr = PatientRegistration()
    detail = User.objects.all()   
    return render(request, 'enroll/addandshow.html', {'form':pr,'det':detail})



# delete
def delete_data(request, id):
    if request.method == 'POST':
        ai = User.objects.get(pk=id)
        ai.delete()
    return HttpResponsePermanentRedirect('/')

# Update

def update_data(request, id):
    if request.method == 'POST':
        ui = User.objects.get(pk=id)
        pr = PatientRegistration(request.POST, instance=ui)
        if pr.is_valid():
            pr.save()
    else:
        ui = User.objects.get(pk=id)
        pr = PatientRegistration( instance=ui)


    return render(request, 'enroll/update.html', {'form': pr})
