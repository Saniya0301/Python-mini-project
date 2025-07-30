from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment


# -------------------------------
# Public Views
# -------------------------------

def About(request):
    return render(request, 'about.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        msg = request.POST.get("msg")
        # Optional: Save to DB or send email
        messages.success(request, "✅ Thank you, your message has been sent!")
    return render(request, "contact.html")


# -------------------------------
# Authentication Views
# -------------------------------

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "❌ Invalid credentials or not authorized.")
    return render(request, 'login.html')


def Logout_admin(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


# -------------------------------
# Admin Dashboard / Protected Views
# -------------------------------

def Index(request):
    if not request.user.is_staff:
        return redirect('login')

    context = {
        'total_doctors': Doctor.objects.count(),
        'total_patients': Patient.objects.count(),
        'total_appointments': Appointment.objects.count(),
    }
    return render(request, 'index.html', context)


def add_doctor(request):
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        specialization = request.POST.get("specialization")
        experience = request.POST.get("experience")
        photo = request.FILES.get("photo")

        # Save doctor
        Doctor.objects.create(
            name=name,
            email=email,
            phone=phone,
            specialization=specialization,
            experience=experience,
            photo=photo
        )
        messages.success(request, "✅ Doctor added successfully!")
        return redirect('add_doctor')

    return render(request, 'add_doctor.html')


def view_patients(request):
    if not request.user.is_staff:
        return redirect('login')

    patients = Patient.objects.all()
    return render(request, 'view_patients.html', {'patients': patients})


def manage_appointments(request):
    if not request.user.is_staff:
        return redirect('login')

    appointments = Appointment.objects.all()
    return render(request, 'manage_appointment.html', {'appointments': appointments})
