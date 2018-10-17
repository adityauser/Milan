from django import forms
from webapp.models import Lost,Found

class LostForm(forms.ModelForm):
	Photo = forms.ImageField(required = True)
	person_name = forms.CharField(required = True)
	provider_email = forms.EmailField(required = True)
	provider_name = forms.CharField(required = True)

	class Meta:
		model = Lost
		fields = ('Photo','person_name','provider_email','provider_name',)
	

class FoundForm(forms.ModelForm):
	Photo = forms.ImageField(required = True)
	location = forms.CharField(required = True)
	condition = forms.CharField(required = True)
	provider_name = forms.CharField(required = True)
	provider_email = forms.CharField(required = True)

	class Meta:
		model = Found
		fields = ('Photo','location','condition','provider_name','provider_email')