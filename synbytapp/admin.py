from django.contrib import admin
from multiupload.admin import MultiUploadAdmin

from .models import (
	SliderImage, 
	Portfolio, 
	Testimonials, 
	Services,
	VoiceAndCarrier,
	AboutUs,
	Support,
	TermsOfUse)

'''
class ImageInline(admin.TabularInline):
    model = SliderText
    insert_after = 'title'


class ModelAAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    inlines = [ImageInline,]
    change_form_template = 'admin/custom/change_form.html'

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }
'''
admin.site.register(SliderImage)
admin.site.register(Portfolio)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(AboutUs)
admin.site.register(Support)
admin.site.register(TermsOfUse)
admin.site.register(VoiceAndCarrier)
#admin.site.register(SliderImage, ModelAAdmin)
