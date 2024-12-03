# ppc_app/views.py
from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PersonDetails, CertificateDetails
from .forms import PersonDetailsForm, CertificateDetailsForm, RegistrationForm


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('/')


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if str(username[0:5]) == (str('admin')):
                user.is_staff = True
                user.is_superuser = True
                user.save()
                login(request, user)
                messages.success(request, 'Admin Registered Successfully')
                return redirect('/')
            else:
                login(request, user)
                messages.success(request, 'Registered Successfully')
                return redirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'ppc_app/register.html', {'form': form})
    return render(request, 'ppc_app/register.html', {'form': form})


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.success(request, 'Invalid username or password')
            return redirect('/')
    return render(request, 'ppc_app/index.html')


def person_list(request):
    if request.user.is_authenticated:
        persons = PersonDetails.objects.all()
        return render(request, 'ppc_app/person_list.html', {'persons': persons})
    else:
        return render(request, 'ppc_app/index.html')


def person_detail(request, userID):
    if request.user.is_authenticated:
        person = get_object_or_404(PersonDetails, userID=userID)
        return render(request, 'ppc_app/person_detail.html', {'person': person})
    else:
        return render(request, 'ppc_app/index.html')



def person_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PersonDetailsForm(request.POST)
            if form.is_valid():
                person = form.save()
                messages.success(request, 'Person record created successfully')
                return redirect('person_detail', userID=person.userID)
        else:
            form = PersonDetailsForm()
        return render(request, 'ppc_app/person_form.html', {'form': form})
    else:
        return render(request, 'ppc_app/index.html')


def person_edit(request, userID):
    if request.user.is_authenticated:
        person = get_object_or_404(PersonDetails, userID=userID)
        if request.method == "POST":
            form = PersonDetailsForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                messages.success(request, 'Person edit successful')
                return redirect('person_detail', userID=person.userID)
        else:
            form = PersonDetailsForm(instance=person)
        return render(request, 'ppc_app/person_form.html', {'form': form})
    else:
        return render(request, 'ppc_app/index.html')


def person_delete(request, userID):
    if request.user.is_superuser:
        person = get_object_or_404(PersonDetails, userID=userID)
        if request.method == 'POST':
            person.delete()
            messages.success(request, 'Person removed successfully')
            return redirect('person_list')
        return render(request, 'ppc_app/person_confirm_delete.html', {'person': person})
    else:
        messages.success(request, 'Delete can only be completed by an admin')
        return render(request, 'ppc_app/index.html')


def certificate_list(request):
    if request.user.is_authenticated:
        certificates = CertificateDetails.objects.all()
        return render(request, 'ppc_app/certificate_list.html', {'certificates': certificates})
    else:
        messages.success(request, 'Must be registered to complete operation')
        return render(request, 'ppc_app/index.html')


def certificate_detail(request, certNumber):
    if request.user.is_authenticated:
        certificate = get_object_or_404(CertificateDetails, certNumber=certNumber)
        return render(request, 'ppc_app/certificate_detail.html', {'certificate': certificate})
    else:
        messages.success(request, 'Must be registered to complete operation')
        return render(request, 'ppc_app/index.html')

def certificate_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CertificateDetailsForm(request.POST)
            if form.is_valid():
                certificate = form.save()
                messages.success(request, 'Certificate created successfully')
                return redirect('certificate_detail', certNumber=certificate.certNumber)
        else:
            form = CertificateDetailsForm()
        return render(request, 'ppc_app/certificate_form.html', {'form': form})
    else:
        messages.success(request, 'Must be registered to complete operation')
        return render(request, 'ppc_app/index.html')


def certificate_edit(request, certNumber):
    if request.user.is_authenticated:
        certificate = get_object_or_404(CertificateDetails, certNumber=certNumber)
        if request.method == "POST":
            form = CertificateDetailsForm(request.POST, instance=certificate)
            if form.is_valid():
                form.save()
                messages.success(request, 'Certificate edit successful')
                return redirect('certificate_detail', certNumber=certificate.certNumber)
        else:
            form = CertificateDetailsForm(instance=certificate)
        return render(request, 'ppc_app/certificate_form.html', {'form': form})
    else:
        messages.success(request, 'Must be registered to complete operation')
        return render(request, 'ppc_app/index.html')


def certificate_delete(request, certNumber):
    if request.user.is_superuser:
        certificate = get_object_or_404(CertificateDetails, certNumber=certNumber)
        if request.method == 'POST':
            certificate.delete()
            messages.success(request, 'Certificate removed successfully')
            return redirect('certificate_list')
        return render(request, 'ppc_app/certificate_confirm_delete.html', {'certificate': certificate})
    else:
        messages.success(request, 'Delete can only be completed by an admin')
        return render(request, 'ppc_app/index.html')

def admin(request):
    if request.user.is_superuser:
        return render(request, 'admin')
    else:
        messages.success(request, 'Admin Login Required')
        return redirect('index')
