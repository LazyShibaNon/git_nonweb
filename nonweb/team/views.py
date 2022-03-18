from django.shortcuts import render, redirect

# Create your views here.

from .forms import UploadModelForm
from .models import team_photo

def index(request):
    
    photos = team_photo.objects.all()
    
    form = UploadModelForm()
    
    if request.method == "POST":
        form = UploadModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/team')
    
    content = {
        "photos" : photos,
        "form" : form
        }
    
    return render(request,'team.html',content)