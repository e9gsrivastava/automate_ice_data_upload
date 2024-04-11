# urls.py
from django.views.generic import TemplateView
from django.urls import path
from .appviews import FileUploadView


app_name = "doc_upload"


urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file_upload"),
    path(
        "upload/success/",
        TemplateView.as_view(template_name="upload_success.html"),
        name="upload_success",
    ),
]
