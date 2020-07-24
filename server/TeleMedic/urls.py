from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Homepage.urls')),
    path('api/auth/', include('UserProfile.urls')),
    path('account/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)