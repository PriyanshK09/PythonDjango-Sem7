# core/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    name = request.GET.get('name', 'Friend')
    return render(request, "home.html", {"name": name})

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # For now, just show a simple response
        return HttpResponse(f"Thank you {name}, we received your message!")
    return render(request, "contact.html")
