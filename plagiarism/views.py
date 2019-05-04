import os
os.environ['DJANGO_SETTINGS_MODULE']='websitepc.settings'
import django
django.setup()
import ast,_ast
from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from plagiarism.forms2 import FilesCreate2
from plagiarism.forms import FilesCreate
from plagiarism.models import File1,Result,File2
def add(request):
    if request.method=='POST':
        form=FilesCreate(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add2'))
    else:
        form=FilesCreate()
        return render(request,'plagiarism/page1.html',{'form':form})

    #return render(request,'plagiarism/page1.html',{'form':FilesCreate})
def add2(request):
    if request.method=='POST':
        form2=FilesCreate2(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('getresult'))
    else:
        form2=FilesCreate2()
        return render(request,'plagiarism/page2.html',{'form':form2})
def getfile1():
    data1=File1.objects.all()
    obj1=data1.get()
    string1=str(obj1)
    file = open("file1.py", "w")
    file.write(string1)
    print("getfile1 in views")
    return 2
def getfile2():
    data2=File2.objects.all()
    obj2=data2.get()
    string2=str(obj2)
    file = open("file2.py", "w")
    file.write(string2)
    print("getfile2 in views")
    return 3
