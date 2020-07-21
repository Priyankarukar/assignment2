from django.shortcuts import render


# Create your views here.
def calpage(request):

    return render(request,"claculate.html")

def getdata(request):
    h=request.GET["Height"]
    w= request.GET["weight"]
    H=float(h)
    W=float(w)
    BMI=W/(H*H)
    return render(request,"claculate.html",{"height":h,"weight":w,'mass':BMI})