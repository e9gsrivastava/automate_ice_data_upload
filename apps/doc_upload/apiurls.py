"""
urls.py
"""
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from .apiviews import FileUpload

urlpatterns = [
    path("file/", FileUpload.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("gettoken/", obtain_auth_token),
]
