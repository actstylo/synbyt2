from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify

	
from django.utils.translation import ugettext_lazy as _

	
class SliderImage(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	description = models.CharField(max_length=120, null=True, blank=True)
	s_image = models.ImageField(upload_to="products", null = True, blank = True, editable = True, help_text = "Slider Image", verbose_name = "Slider Image")
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="1500")
	
	def __str__(self):
		return self.title
		
class Portfolio(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	url = models.CharField(max_length=100, null=True, blank=True, editable=True, help_text='Website Address', verbose_name='Website')
	p_image = models.ImageField(upload_to="products", null = True, blank = True, editable = True, help_text='Portfolio Image')
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	
	def __str__(self):
		return self.title
		
class Testimonials(models.Model):
	description = models.CharField(max_length=200, null=True, blank=True, help_text='Your Recommendation')
	name = models.CharField(max_length=100, null=True, blank=True, help_text="Key Person Name")
	company_name = models.CharField(max_length=200, null=True, blank=True, help_text="Company Name")
	website = models.CharField(max_length=200, null=True, blank=True, help_text="Company Website")
	t_image = models.ImageField(upload_to="products", null = True, blank = True, editable = True, help_text="Key Person Image")
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="135")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="135")
	
	def __str__(self):
		return self.name
		
class Services(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True, help_text='Service Title')
	description = models.CharField(max_length=100, null=True, blank=True, help_text='Service Description')
	s_image = models.ImageField(upload_to="products", null = True, blank = True, editable = True, help_text='Portfolio Image')
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	
	def __str__(self):
		return self.title
		
class VoiceAndCarrier(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True, help_text='Service Title')
	description = models.CharField(max_length=100, null=True, blank=True, help_text='Service Description')
	s_image = models.ImageField(upload_to="products", null = True, blank = True, editable = True, help_text='Portfolio Image')
	image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
	
	def __str__(self):
		return self.title
		
class AboutUs(models.Model):
	title = models.CharField(max_length=200, blank=False, help_text='About Us Title')
	description = models.TextField(max_length=2000, null=True, blank=True, help_text='About Us')
	
	def __str__(self):
		return self.title
		
class Support(models.Model):
	title = models.CharField(max_length=200, blank=False, help_text='Support Title')
	description = models.TextField(max_length=2000, null=True, blank=True, help_text='Support')
	
	def __str__(self):
		return self.title
		
class TermsOfUse(models.Model):
	title = models.CharField(max_length=200, blank=False, help_text='Support Title')
	description = models.TextField(max_length=2000, null=True, blank=True, help_text='Support')
	
	def __str__(self):
		return self.title
	
		
'''
class SliderImage(models.Model):
	title = models.CharField(verbose_name=_('title'), max_length=255, blank=True, null=True)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
	
	def __str__(self):
		return self.title

class SliderText(models.Model):
	model_a = models.ForeignKey('SliderImage', verbose_name='Slider Image')
	image = models.ImageField(upload_to='images/')
'''