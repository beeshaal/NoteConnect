from . import views
from django.urls import path

urlpatterns = [
    path('',views.qna_home,name="qna_home"),
    path('ask_question/',views.ask_question,name='ask_question'),
    path('view-post/',views.viewpost,name='viewpost'),
    path('my-posts/',views.myposts,name='myposts'),
    path('delete-post/<int:id>',views.delete_post,name='delete_post'),
    path('edit-post/<int:id>',views.editpost,name='edit_post'),
    path('post-comment/<int:id>',views.post_comment,name='post_comment'), 
    path('notifications/',views.handle_notifications,name="handle_notifications"),
    # path('search-posts/',views.search_posts,name="search_posts"),
]
