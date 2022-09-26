
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import PatientInfo, UserProfile, RegisteredPatient
from .form import PatientForm, AddInPatient



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class FreeForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/form.html')   

class MainForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/main-form.html')   

class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'content/mainPage.html')

class FormWithPatient(View):
    def get(self, request, *args, **kwargs):
        patient = PatientInfo.objects.all()
        p_name = RegisteredPatient.objects.all()
        # form = AddInPatient()
        context = {
            'patients':patient,
            'p_name':p_name
            # 'form':form
        }
        return render(request, 'content/formwithpatient.html', context)


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        patients = PatientInfo.objects.all()

        context = {
            'profile': profile,
            'patients': patients
        }
        return render(request, 'content/profile.html', context)        
  
## Adding patient to database 
class AddPatientPage(View):
    def post(self, request, *args, **kwargs):
        form = PatientForm()
        submitted = False
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('sadd-patient?submitted=True')
        else:
            form = PatientForm()
            if 'submitted' in request.GET:
                submitted = True
        context = {
            'form':form,
            'submitted':submitted
            }        
        return render(request, 'content/add-patient.html', context)

    def get(self, request, *args, **kwargs):
        form = PatientForm()
        context = {'form':form}
        return render(request, 'content/add-patient.html', context)     

               