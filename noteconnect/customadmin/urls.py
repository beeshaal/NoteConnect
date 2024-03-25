from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('pending-notes',views.pending_notes,name='pending_notes'),
    path('accepted-notes',views.accepted_notes,name='accepted_notes'),
    path('rejected-notes',views.rejected_notes,name='rejected_notes'),
    path('signout',views.signout,name="signout"),
    path('assign-accepted/<int:pid>',views.assign_accepted,name='assign_accepted'),
    path('assign-rejected/<int:pid>',views.assign_rejected,name='assign_rejected'),
    path('send-message',views.submit_message,name='submit_message'),
    path('user_messages',views.user_messages,name="user_messages"),


]