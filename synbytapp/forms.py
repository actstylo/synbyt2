from django import forms

class AboutUs(forms.ModelForm):
	text = forms.CharField(
		widget = forms.Textarea(
			attrs={'rows': 10, 'placeholder': 'About Us'}
		),
		max_length=10000,
		help_text='About Us in 10000 words.'
	)
	
class Privacy(forms.ModelForm):
	pass
	
class CopyrightGuidelines(forms.ModelForm):
	pass
	
class TermsOfUse(forms.ModelForm):
	pass