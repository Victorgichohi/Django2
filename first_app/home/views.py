from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponse
from .forms import FeedBackform
from .models import student
# Create your views here.
def index(request):
		return render(request,'index.html', context)
		

def reques(request):
	form = StudentForm(request.POST or None)
	context={
	"hello_message" :"Register?",
	"form":form
     }
	if form.is_valid():
		form.save()
		context={
		    "hello_message":"You've been saved:-)"
          }

def feedback(request):

	form=FeedBackform()
	context={
	   "form":form
	}
	return render(request, 'feedback.html' ,context)

def students(request):
	search_term=request.GET.get('search', default='')
	students = student.objects.all().order_by('-last_update').filter(full_name__contains=search_term)
	context={
	'students' : students
	}
	return render(request, 'students.html' ,context)
