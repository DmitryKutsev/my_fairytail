from django.shortcuts import render

# Create your views here.


def greeting_view(request):
    """Simple greeting view that renders a beautiful front page"""
    return render(request, "fairytales/frontpage.html")
