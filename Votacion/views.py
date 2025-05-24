from django.shortcuts import render

def create_votation(request):
    return render(request,'Votacion/home.html')