from django.contrib import admin
from .models import student
from .forms import StudentForm
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	form=StudentForm

admin.site.register(student, StudentAdmin)
