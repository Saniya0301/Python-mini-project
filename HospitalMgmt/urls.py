from django.contrib import admin
from django.urls import path
from hospital.views import About, Index, Login, Logout_admin, Contact
import hospital.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('', Index, name='home'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),

    # Avoid Django admin path conflict
    path('hospital/add-doctor/', views.add_doctor, name='add_doctor'),
    path('hospital/view-patients/', views.view_patients, name='view_patients'),
    path('hospital/manage-appointments/', views.manage_appointments, name='manage_appointments'),
]
