from django.contrib import admin

from blog.models import Doctor, Patient, Appointment

class AppointmentInline(admin.StackedInline):
    model = Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        AppointmentInline,
    ]

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)

# Register your models here.
