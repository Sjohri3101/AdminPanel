from django.shortcuts import render

# Create your views here.
def alert_home(request):
    return render(request,"alert/alert_home.html")