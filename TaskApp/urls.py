from django.urls import path, include
from django.conf.urls import url
from . import views
from allauth.account.views import confirm_email

urlpatterns = [
    url(r'shift/', views.ShiftView.as_view()),
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'rest-auth/register', include('rest_auth.registration.urls')),
]
 