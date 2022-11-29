from django.shortcuts import render

# Create your views here.


def a1_first(request):
    d={'a':10,'b':100}
    return render(request,'a1_first.html',context=d)

def a1_second(request):
    d={'a':10,'b':100,'c':200}
    return render(request,'a1_second.html',context=d)

def a2_first(request):
    d={'a':10,'b':100,'c':200}
    return render(request,'a2_first.html',context=d)

def a2_second(request):
    return render(request,'a2_second.html')