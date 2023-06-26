from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Notes
from django.contrib.auth.models import User
from datetime import date
from django.contrib import messages

def uploadnotes(request):
    if request.method == 'GET':
        return render(request,'upload_note.html')
    
    if request.method == 'POST':
        program = request.POST['program']
        course = request.POST['course']
        file = request.POST['file']
        filetype = request.POST['filetype']
        description = request.POST['description']
        user = User.objects.filter(username=request.user.username).first()
        newnote = Notes.objects.create(user=user,upload_date= date.today(),program=program,course=course,notesfile=file,filetype=filetype,description=description,status='pending')
        newnote.save()
        messages.success(request,'Notes uploaded successfully!')
        return redirect('viewnotes')

def viewnotes(request):
    allnotes = Notes.objects.all()
    context = {'allnotes': allnotes}
    return render(request,'viewallnotes.html',context)