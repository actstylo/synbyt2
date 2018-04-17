from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from synbytapp import views
from accounts import views as accounts_views

from django.conf.urls import (
handler400, handler403, handler404, handler500
)

handler400 = 'synbytapp.views.bad_request'
handler403 = 'synbytapp.views.permission_denied'
handler404 = 'synbytapp.views.page_not_found'
handler500 = 'synbytapp.views.server_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^support/$', views.support, name='support'),
	url(r'^terms/$', views.terms_of_use, name='terms_of_use'),
	
	url(r'^contact/$', accounts_views.contact, name='contact'),
	url(r'^success/$', accounts_views.successView, name='success'),
	
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	
	url(r'^reset/$',
		auth_views.PasswordResetView.as_view(
			template_name='password_reset.html',
			email_template_name='password_reset_email.html',
			subject_template_name='password_reset_subject.txt'
		), name='password_reset'),
	url(r'^reset/done/$',
		auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
		name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
		name='password_reset_confirm'),
	url(r'^reset/complete/$',
		auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
		name='password_reset_complete'),		
	url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
		name='password_change'),
	url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
		name='password_change_done'),
]
if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)