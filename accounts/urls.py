from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "accounts"
urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'profile/change_password$', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
