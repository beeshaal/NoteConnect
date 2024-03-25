from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib  import messages
from notes.models import Notes
from main.models import Contact
from django.shortcuts import get_object_or_404

def call_context():
    pending_notes = Notes.objects.filter(status='pending')
    accepted_notes = Notes.objects.filter(status='accepted')
    rejected_notes = Notes.objects.filter(status='rejected')
    user_messages = Contact.objects.all()
    context1 = {
        'pn': pending_notes,
        'an': accepted_notes,
        'rn': rejected_notes,
        'um': user_messages,
    }
    context2 = {
        'pn_count': pending_notes.count(),
        'an_count': accepted_notes.count(),
        'rn_count': rejected_notes.count(),
        'um_count': user_messages.count(),
    }
    context = {'context1':context1,'context2': context2}
    return context


def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Login required!")
        return redirect('admin_login')
    context = call_context()
    return render(request,'admin_dashboard.html',context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        if user and user.is_superuser:
            login(request,user)
            messages.success(request,'Admin Login Success!')
            return redirect('admin_dashboard')
        else:
            messages.error(request,"Admin not recognized!")
            return render(request,'admin_login.html')
        
    else:
        return render(request,'admin_login.html')
        
def pending_notes(request):
    pending_notes = Notes.objects.filter(status='pending')
    context = call_context()
    context['notesnotfound']= 'No pending notes!'
    if pending_notes:
        return render(request,'notes/pending_notes.html',context)
    else:
        return render(request,'notes/no_notes_admin.html',context)

def accepted_notes(request):
    accepted_notes = Notes.objects.filter(status='accepted')
    context = call_context()
    context['notesnotfound']= 'No accepted notes!'
    if accepted_notes:
        return render(request,'notes/accepted_notes.html',context)
    else:
        return render(request,'notes/no_notes_admin.html',context)

def rejected_notes(request):
    rejected_notes = Notes.objects.filter(status='rejected')
    context = call_context()
    context['notesnotfound']= 'No rejected notes!'
    if rejected_notes:
        return render(request,'notes/rejected_notes.html',context)
    else:
        return render(request,'notes/no_notes_admin.html',context)

def user_messages(request):
    user_messages = Contact.objects.all()
    context = call_context()
    context['notesnotfound']= 'No user feedbacks!'
    if user_messages:
      return render(request,'user_messages.html',context)
    else:
      return render(request,'notes/no_notes_admin.html',context)

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('admin_login')

def assign_accepted(request, pid):
    note = get_object_or_404(Notes, id=pid)
    note.status = 'accepted'
    note.save()
    context = {'pn': [note]} 
    return redirect('rejected_notes')

def assign_rejected(request, pid):
    note = get_object_or_404(Notes, id=pid)
    note.status = 'rejected'
    note.save()
    context = {'pn': [note]} 
    return redirect('accepted_notes')

def submit_message(request):
    if request.method=='POST':
        name = request.POST['name']
        email =request.POST['email']
        message = request.POST['message']
        new_message = Contact.objects.create(name=name,email=email,message=message)
        new_message.save()
        messages.success(request,'Message Sent Successfully!')
        return redirect('home')
    return HttpResponse('something went wrong!')

