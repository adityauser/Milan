from django import forms
from webapp.models import Lost,Found

class LostForm(forms.ModelForm):
	Photo = forms.FileField(required = False)
	person_name = forms.CharField(required = True)
	provider_email = forms.EmailField(required = True)
	provider_name = forms.CharField(required = True)
	provider_number = forms.CharField(required = True)

	class Meta:
		model = Lost
		fields = ('Photo','person_name','provider_email','provider_name','provider_number',)
	

class FoundForm(forms.ModelForm):
	Photo = forms.FileField(required = False)
	location = forms.CharField(required = True)
	condition = forms.CharField(required = True)
	provider_name = forms.CharField(required = True)
	provider_email = forms.CharField(required = True)
	provider_number = forms.CharField(required = True)

	class Meta:
		model = Found
		fields = ('Photo','location','condition','provider_name','provider_email','provider_number',)

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()