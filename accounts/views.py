from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
#from django.core.mail import EmailMessage
#from django.template import Context
#from django.template.loader import get_template

from .forms import SignUpForm, ContactForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
	
def contact(request):
	if request.method == 'GET':
		form = ContactForm()
		
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			contact_email = form.cleaned_data['contact_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, contact_email, ['rezaulwilldoeverythisac@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, 'contact.html', {'form': form})
	
def successView(request):
	return render(request, 'success.html')