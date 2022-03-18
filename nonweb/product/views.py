from django.shortcuts import render

# Create your views here.

from .models import Products

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger




def products(request):
    
    pname=""
    if 'qp' in request.GET:
        
        pname = request.GET['qp']
        pData = Products.objects.filter(name__contains=pname)        
    else:    
        pData = Products.objects.all().order_by('-id')
    
    #pData = Products.objects.all().order_by('-id')[:10]  #抓排序後的前10筆資料
    #pData = Products.objects.filter(price='2084')

    paginator = Paginator(pData,8)
    #page = request.GET['page']
    page = request.GET.get('page')


    try:
        pData = paginator.page(page)
    except PageNotAnInteger:
        pData = paginator.page(1)
        
    except EmptyPage:
        pData = paginator.page(paginator.num_pages)
    
    
    content = {'product':pData,'pname':pname}
    return render(request,'product.html',content)