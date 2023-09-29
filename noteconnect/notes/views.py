from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Notes
from django.contrib.auth.models import User
from datetime import date
from django.contrib import messages
from django.conf import settings

coursecodelist = {
    'Engineering Mathematics I':'MTH111',
    'Chemistry':'CHM103',
    'Communication Technique':'ENG104',
    'Programming in C':'CMP103',
    'Basic Electrical Engineering':'ELE105',
    'Mechanical Workshop':'MEC178',
    'Engineering Mathematics II':'MTH121',
    'Physics': 'PHY102',
    'Engineering Drawing':'MEC109',
    'Object Oriented Programming in C++':'CMP104',
    'Thermal Science':'MEC189',
    'Applied Mechanics':'MEC119',
    'Engineering Mathematics III':'MTH211',
    'Data Structure and Algorithm':'CMP331',
    'Electrical Engineering Materials':'ELE226',
    'Network Theory':'ELE215',
    'Electronic Devices':'ELX213',
    'Logic Circuits':'ELX212',
    'Engineering Mathematics IV':'MTH223',
}

def uploadnotes(request):
    if request.method == 'GET':
        return render(request,'notes/upload_note.html')
    
    if request.method == 'POST':
        file = request.FILES['file']
        if file is not None:
            if file.size > settings.DATA_UPLOAD_MAX_MEMORY_SIZE:
                messages.error(request,'File size exceeded the limit')
                return redirect('uploadnotes')
        program = request.POST['program']
        semester = request.POST['semester']
        course = request.POST['course']
        coursecode = coursecodelist[course]
        filetype = request.POST['filetype']
        description = request.POST['description']
        user = User.objects.filter(username=request.user.username).first()
        newnote = Notes.objects.create(user=user,upload_date= date.today(),program=program,semester=semester,course=course,coursecode=coursecode,notesfile=file,filetype=filetype,description=description,status='pending')
        newnote.save()
        messages.success(request,'Submitted For Approval!')
        return redirect(myuploads)

def viewnotes(request,course_code):
    allnotes = Notes.objects.filter(coursecode=course_code).filter(status='accepted')
    context1 = {'allnotes': allnotes}
    context2 = {'notesnotfound':'Notes not found!'}
    if allnotes:
        return render(request,'notes/view-notes.html',context1)
    else:
        return render(request,'notes/no_uploads.html',context2)

def notes_home(request):
    return render(request,'notes/notes_navigation.html')

def myuploads(request):
    user = User.objects.get(id= request.user.id)
    mynotes = Notes.objects.filter(user=user)
    if mynotes.count() == 0:
        context1 = {'notesnotfound': 'You have not uploaded yet!'}
        return render(request,'notes/no_uploads.html',context1)
    else:
        context2={'mynotes': mynotes}
        return render(request,'notes/viewmynotes.html',context2)

def view_programs(request):
   return render(request,'notes/view_programs.html')

def search_notes(request):
    if request.method=='GET':
        return redirect('notes_home')
    if request.method=='POST':
        search_field = request.POST['search']
        course_code = search_field.strip().upper().replace(" ", "")
        allnotes = Notes.objects.filter(coursecode=course_code).filter(status='accepted')
        context={'allnotes': allnotes }
        return render(request,'notes/view-notes.html',context)
    messages.error(request,'Something wrong occured')
    return redirect('notes_home')

def delete_note(request, id):
    obj = Notes.objects.get(id=id)
    obj.delete()
    messages.success(request,'Note deleted successfully!')
    return redirect('myuploads')

def render_programs(request):
    if request.method=='POST':
        selected_program = request.POST['program']
        if (selected_program == 'BE Computer'):
            return redirect('render_computer')
        elif (selected_program == 'BE Civil'):
            return redirect('render_civil')
        elif (selected_program == 'BE Software'):
            return redirect('render_software')
        elif (selected_program == 'BE IT'):
            return redirect('render_it')
        else:
            return redirect('render_bca')
    return HTTPResponse('Something went wrong')

def render_computer(request):
    return render(request,'notes/program/computer.html')
def render_software(request):
    return render(request,'notes/program/software.html')
def render_civil(request):
    return render(request,'notes/program/civil.html')
def render_it(request):
    return render(request,'notes/program/it.html')
def render_bca(request):
    return render(request,'notes/program/bca.html')