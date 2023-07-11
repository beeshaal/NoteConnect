from . import views
from django.urls import path

urlpatterns = [
    path('',views.notes_home,name="notes_home"),
    path('computer',views.render_computer,name='render_computer'),
    path('upload-notes',views.uploadnotes,name="uploadnotes"),
    path('view-note/<str:course_code>',views.viewnotes,name="viewnotes"),
    path('my-uploads',views.myuploads,name="myuploads"),
    path('view-programs',views.view_programs,name='view_programs'),
    path('search-notes',views.search_notes,name='search_notes'),
    path('delete-note/<int:id>',views.delete_note,name='delete_note'),
    path('view-progams',views.render_programs,name='render_programs'),
    path('civil',views.render_civil,name='render_civil'),
    path('software',views.render_software,name='render_software'),
    path('it',views.render_it,name='render_it'),
    path('bca',views.render_bca,name='render_bca'),
]
