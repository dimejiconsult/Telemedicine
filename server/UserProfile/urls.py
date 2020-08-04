from django.urls import path, include
from django.conf.urls import url
from allauth.account.views import confirm_email
from .views import LoginAPIView, RegisterAPIView, ProfileAPI
from knox import views as knox_view
urlpatterns = [
    path('', include('knox.urls')),
    path('users', ProfileAPI.as_view()),
    path('register', RegisterAPIView.as_view()),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    path('login', LoginAPIView.as_view()),
    path('logout', knox_view.LogoutView().as_view(), name='knox_logout')
]
