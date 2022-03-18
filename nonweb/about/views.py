from django.shortcuts import render

# Create your views here.

from .models import Reviews
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def menu(request):
    return render(request,"menu.html")

def about(request):
    
    all_reviews = Reviews.objects.all().order_by('id')[:30]
    
    paginator = Paginator(all_reviews,3)
    page = request.GET.get('page')
    
    try:
        all_reviews = paginator.page(page)
    except PageNotAnInteger:
        all_reviews = paginator.page(1)
    except EmptyPage:
        all_reviews = paginator.page(paginator.num_pages)
    
    content ={"reviews":all_reviews}       
    return render(request,"about.html",content)