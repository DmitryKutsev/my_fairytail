from django.shortcuts import render
from django.db.models import Q
from .models import FairyTale, Language

# Create your views here.


def greeting_view(request):
    """Simple greeting view that renders a beautiful front page"""
    return render(request, "fairytales/frontpage.html")


def search_view(request):
    """Search view that handles filtering and displays results"""
    tales = FairyTale.objects.all()
    
    # Get search parameters
    keyword = request.GET.get('keyword', '').strip()
    author = request.GET.get('author', '').strip()
    language_code = request.GET.get('language', '').strip()
    origin = request.GET.get('origin', '').strip()
    
    # Apply filters
    if keyword:
        tales = tales.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        )
    
    if author:
        tales = tales.filter(author=author)
    
    if language_code:
        tales = tales.filter(language__code=language_code)
    
    if origin:
        tales = tales.filter(land_of_origin=origin)
    
    # Order by title
    tales = tales.order_by('title')
    
    context = {
        'tales': tales,
    }
    
    return render(request, 'fairytales/search.html', context)
