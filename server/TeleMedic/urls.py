from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('home', include('Homepage.urls')),
    path('api/auth/', include('UserProfile.urls')),
    path('account/', include('allauth.urls')),
    path('graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('admin/', admin.site.urls),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)