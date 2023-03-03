from django.shortcuts import render

def staticfile(request):
    return render(request,'staticfile.html')

def staticfile2(request):
    return render(request,'staticfile2.html')