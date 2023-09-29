from datetime import date,datetime
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse

def calculate_time_difference(post):
    now = timezone.now()
    uploaded_time = post.uploaded_on

    time_difference = now - uploaded_time
    return time_difference


def format_time_difference(time_difference):
    days = time_difference.days
    seconds = time_difference.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days >= 7:
        weeks, days = divmod(days, 7)
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif days > 0:
        return f"{days} day{'s' if days > 1 else ''} ago"
    elif hours > 0:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif minutes > 0:
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "just now"
    

def qna_home(request):
    return render(request,'qna/qna_home.html')

def ask_question(request):
    if request.method == 'GET':
        return render(request,'qna/create_post.html')
    
    if request.method == 'POST':
        course = request.POST['course']
        title = request.POST['title']
        description = request.POST['description']
        user = User.objects.filter(username=request.user.username).first()
        newpost = Post.objects.create(uploaded_by=user,uploaded_on= date.today(),course=course,title=title,description=description)
        newpost.save()
        messages.success(request,'Submitted For Approval!')
        return redirect('myposts')

def myposts(request):
    myallposts = Post.objects.filter(uploaded_by=request.user)
    user = request.user
    if user.is_superuser:
        fullname = "Admin"
    else:
        fullname = user.first_name + " " + user.last_name
    for post in myallposts:
        time_difference = calculate_time_difference(post)
        formatted_time = format_time_difference(time_difference)
        post.formatted_time = formatted_time
        post.fullname = fullname
    context={'myallposts': myallposts}
    context2={'nopost_message': "No posts Yet!"}
    if myallposts.count():
       return render(request,'qna/my_posts.html',context)  
    else:
        return render(request,'qna/no_posts.html',context2)
    
def delete_post(request, id):
    obj = Post.objects.get(id=id)
    obj.delete()
    messages.success(request,'Post deleted successfully!')
    return redirect('myposts')

def editpost(request,id):
    if request.method=='GET':
        post_to_be_edited = Post.objects.get(id=id)
        context={'editvalues':post_to_be_edited}
        return render(request,'qna/edit_post.html',context)

    elif request.method=='POST':
        new_course = request.POST['course']
        new_title = request.POST['title']
        new_description = request.POST['description']
        post_to_be_updated = Post.objects.get(id=id)
        post_to_be_updated.course=new_course
        post_to_be_updated.title=new_title
        post_to_be_updated.description=new_description
        post_to_be_updated.save()
        messages.success(request,'Post updated successfully!')
        return redirect('myposts')
    
    else:
        return HttpResponse("Oops! Something went wrong.")


def viewpost(request):
    if request.method=='POST':
         search_field_data = request.POST['search']
         allposts = Post.objects.filter(course__icontains=search_field_data) | Post.objects.filter(title__icontains=search_field_data) | Post.objects.filter(description__icontains=search_field_data)
    else:
        allposts = Post.objects.all()
    for post in allposts:
        user=post.uploaded_by
        fullname=user.first_name + " " + user.last_name
        time_difference = calculate_time_difference(post)
        formatted_time = format_time_difference(time_difference)
        post.formatted_time = formatted_time
        allcomments= Comment.objects.filter(post=post)
        for comment in allcomments:
            time_diff = calculate_time_difference(comment)
            formatted_time = format_time_difference(time_diff)
            comment.formatted_time = formatted_time
            user=comment.user
            fullname=user.first_name + " " + user.last_name
            if not user.is_superuser:
               comment.fullname = fullname
            else:
                comment.fullname ="Admin"
        post.allcomments = allcomments
        comment_count = allcomments.count()
        post.comment_count = comment_count
        if user.is_superuser:
           post.fullname = "Admin"
        else :
           post.fullname=fullname
    context={'accepted_posts':allposts}
    return render(request,'qna/view_post.html',context)  


def post_comment(request, id):
    if request.method == 'POST':
        content = request.POST['comment']
        user = request.user  # Get the current user
        post = Post.objects.get(id=id)  # Get the Post instance by id

        comment_obj = Comment.objects.create(
            content=content,
            post=post,
            user=user,
            uploaded_on=date.today()
        )
        return redirect('viewpost')

# def handle_notifications(request):
#     myallposts = Post.objects.filter(uploaded_by=request.user)
#     for post in myallposts:
#         allcomments_in_mypost = Comment.objects.filter(post=post)
#         for comment in allcomments_in_mypost:
#             commented_by = comment.user
#             if commented_by.is_superuser:
#                fullname = "Admin"
#             else:
#                fullname = commented_by.first_name + " "+ commented_by.last_name
#             comment.fullname = fullname
#     context = {'allcomments':allcomments_in_mypost}
#     return render(request,'qna/view_notifications.html',context)

def handle_notifications(request):
    myallposts = Post.objects.filter(uploaded_by=request.user)
    allcomments_in_mypost = Comment.objects.none()  # Initialize as an empty queryset
    
    for post in myallposts:
        allcomments_in_mypost = allcomments_in_mypost | Comment.objects.filter(post=post)  # Update with comments
    
        for comment in allcomments_in_mypost:
            commented_by = comment.user
            if commented_by is not request.user:
                if commented_by.is_superuser:
                   comment.fullname = "Admin"
                else:
                   comment.fullname = commented_by.first_name + " "+ commented_by.last_name
            else:
              comment.fullname = "You"
            time_diff = calculate_time_difference(comment)
            formatted_time = format_time_difference(time_diff)
            comment.formatted_time = formatted_time
            
    context1 = {'allcomments': allcomments_in_mypost}
    context2 = {'nopost_message': "No Notifications yet!"}
    if allcomments_in_mypost:
        return render(request, 'qna/view_notifications.html', context1)
    else:
        return render(request, 'qna/no_posts.html', context2)
    
def search_posts(request):
    if request.method == 'POST':
        search_field_data = request.POST['search']
        search_results = Post.objects.filter(course__icontains=search_field_data) | Post.objects.filter(title__icontains=search_field_data) | Post.objects.filter(description__icontains=search_field_data)
        