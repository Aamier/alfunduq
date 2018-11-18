from django.urls import path, include
from .custom_auth import CustomLoginView
from django.conf.urls import url

urlpatterns = [
    path('users/', include('users.urls')),
    path('configure/', include('configure.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/$', CustomLoginView.as_view())
]
