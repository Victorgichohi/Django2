from django import forms
from .models import student

class StudentForm(forms.ModelForm):
	class Meta:
		#fields=('full_name','email','age')
		exclude=['last_update']
		model=student
	def clean_age(self):
		age=self.cleaned_data.get('age')

		if age > 120:
			raise forms.ValidationError("You too old for this class")
		elif age < 12:
		    raise forms.ValidationError("You too young for this class")
		return age
class FeedBackform(forms.Form):
	full_name=forms.CharField()
	email=forms.EmailField()
	message=forms.CharField(widget=forms.Textarea)
