from . import views
from django.urls import path,include

urlpatterns = [
    path('upload-notes',views.uploadnotes,name="uploadnotes"),
    path('view-notes',views.viewnotes,name="viewnotes"),
]
