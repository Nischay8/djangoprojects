
from django.shortcuts import render
from .forms import StudentRegistraions
from .models import user
from django.http import HttpResponseRedirect
# Create your views here.
#this function will add new Item and shows 
def add_show(request):
    if request.method =='POST':
        fm=StudentRegistraions(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentRegistraions()
    stud= user.objects.all()
    return render(request,'addandshow.html',{'form':fm,
    'stu':stud})


#this function will delete 
def delete_data(request,id):
    if request.method =='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#this Function will update/Edit
def update_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=StudentRegistraions(request.POST,instance=pi)
        if fm.is_valid():
              fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=StudentRegistraions(instance=pi)

    return render(request,'updatestudent.html',{'form':fm})