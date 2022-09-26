from django.urls import path
from inputs.views import FormWithPatient, Index, FreeForm, MainPage, MainForm, AddPatientPage, ProfileView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('form/', FreeForm.as_view(), name='form'),
    path('mainpage/', MainPage.as_view(), name='mainpage'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('add-patient/', AddPatientPage.as_view(), name='add-patient'),
    path('mainform/', MainForm.as_view(), name='mainform'),
    path('patientform/', FormWithPatient.as_view(), name='patientform'),
]