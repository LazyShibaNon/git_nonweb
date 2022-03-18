from django.shortcuts import render

# Create your views here.

import requests
from bs4 import BeautifulSoup

from .recipe import Icook

def recipe(request):
    
    icook = Icook(request.POST.get("search"))
    
    content = {"items":icook.scrape()} # scrape() 網頁爬取
    
    return render(request,"recipe.html",content)
    


