from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from webapp.forms import LostForm,FoundForm
from webapp.face import find_similar

class HomeView(TemplateView):
	template_name = 'landing.html'



class LostView(TemplateView):
	template_name = 'lost.html'

	def get(self,request):
		form = LostForm()
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = LostForm(request.POST, request.FILES)
		if form.is_valid():
			
			Photo = form.cleaned_data['Photo']
			person_name = form.cleaned_data['person_name']
			provider_email = form.cleaned_data['provider_email']
			provider_name = form.cleaned_data['provider_name']
			obj = form.save()
			# ..............for email .............
			subject = "Lost"
			from_email = settings.EMAIL_HOST_USER
			message = "We will inform as soon as you loved one is found"
			to_list = [provider_email]

			send_mail(subject,message,from_email,to_list,fail_silently=False)
			#print("mail sent")
			# ..................................................

			
			# need to incorporate methods to call api and send mail if found 
			

			return redirect('home')

		args = {'form':form}
		return render(request,self.template_name,args)



class FoundView(TemplateView):
	template_name = 'found.html'

	def get(self,request):
		form = FoundForm()
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = FoundForm(request.POST, request.FILES)

		if form.is_valid():
			Photo = form.cleaned_data['Photo']
			location = form.cleaned_data['location']
			condition = form.cleaned_data['condition']
			provider_email = form.cleaned_data['provider_email']
			provider_name = form.cleaned_data['provider_name']
			form.save()

			# ..............for email .............

			subject = "No repy"
			from_email = settings.EMAIL_HOST_USER
			message = "Thank you we will update you as soon as we get info about the person "
			to_list = [provider_email]

			send_mail(subject, message, from_email, to_list, fail_silently=False)
			# ..................................................

			# need to incoporate methods to call api and send mail if found

			return redirect('home')

		args = {'form':form}
		return render(request,self.template_name,args)