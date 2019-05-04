from django.shortcuts import render
def check(request):
    data=95.3
    d=data
    return render(request,'plagiarism/page3.html',{'data':d})