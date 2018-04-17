from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(required=True, widget=forms.Textarea)
	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Your name:'
		self.fields['contact_email'].label = 'Your email:'
		self.fields['subject'].label = 'Subject:'
		self.fields['message'].label = 'Message:'