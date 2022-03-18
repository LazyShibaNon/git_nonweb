from django.shortcuts import render , redirect
from cart import models
from product.models import Products


# Create your views here.

cartlist = list()
customname = ""
customphone = ""
customaddress = ""
customemail = ""

def cart(request): #顯示購物車內容
    global cartlist
    allcart = cartlist
    total = 0
    for unit in cartlist: # 計算商品總額
        total += int(unit[3])  # customname 在 OrdersModel 裡是第四個 (最前面還有一個 id)
    grandtotal = total + 60 # 有加運費
    return render(request,"cart.html",locals())


def addtocart(request,ctype=None,productid=None):
    global cartlist
    if ctype == "add" : # 定義加入購物車
        product = Products.objects.get(id=productid)
        flag = True
        for unit in cartlist:
            if product.name == unit[0]: # 若商品存在的話
                unit[2] = str(int(unit[2])+1) # 數量加1
                unit[3] = str(int(unit[3])+ product.price) # 累加金額
                flag = False; # 表示商品之前已存在於購物車中
                break
        if flag: # 代表商品沒有存在於購物車
            templist = list()
            templist.append(product.name) # 商品名
            templist.append(str(product.price)) # 商品價格
            templist.append("1") # 數量
            templist.append(str(product.price)) # 總價
            cartlist.append(templist)
                
        request.session["cartlist"] = cartlist # 將購物車內容存入session
        return redirect('/cart/')
    elif ctype == "update":  # 更新購物車商品數量
        n = 0
        for unit in cartlist:
            unit[2] = request.POST.get("qty"+str(n),"1") # 取得數量
            unit[3] = str(int(unit[1])*int(unit[2])) # 總價
            n += 1
        request.session["cartlist"] = cartlist # 將購物車內容存入session
        return redirect('/cart/')
    elif ctype =="empty": # 清空購物車
        cartlist = list()
        request.session["cartlist"] = cartlist 
        return redirect("/cart/")
    elif ctype == "remove": # 刪除購物車中的某一項商品
        del cartlist[int(productid)]
        request.session["cartlist"] = cartlist 
        return redirect('/cart/')


def cartorder(request): # 結帳


    global cartlist , customname ,customphone , customaddress , customemail
    allcart = cartlist
    total = 0
    for unit in cartlist:
        total += int(unit[3])
    grandtotal = total + 60
    name = customname
    phone = customphone
    address = customaddress
    email = customemail
    return render(request,"cartorder.html",locals())

   


def cartok(request): # 最後確認買單
    global cartlist , customname ,customphone , customaddress , customemail
    total = 0
    for unit in cartlist:
        total += int(unit[3])
    grandtotal = total + 60
    
    customname = request.POST.get("CuName","")
    customphone = request.POST.get("CuPhone","")
    customaddress = request.POST.get("CuAddr","")
    customemail = request.POST.get("CuEmail","")
    payType = request.POST.get("payType","")
    
    unitorder = models.OrdersModel.objects.create(subtotal=total,shipping=60,grandtotal=grandtotal,customname=customname,customphone=customphone,customemail=customemail,customaddress=customaddress,paytype=payType) #建立訂單
    for unit in cartlist:
        total = int(unit[1]) * int(unit[2])            #關聯式，訂單刪除跟著刪除
        unitdetail = models.DetailModel.objects.create(dorder=unitorder,pname=unit[0],unitprice=unit[1],quantity=unit[2],dtotal=total)
    orderid = unitorder.id # 取得訂單編號
    name = unitorder.customname #取得購買者姓名
    email = unitorder.customemail #取得購買者Email
    cartlist = list()
    request.session["cartlist"] = cartlist
    return render(request,"cartok.html",locals())
                
def cartordercheck(request): # 查詢訂單
    orderid = request.GET.get('orderid','') # 取訂單編號
    customemail = request.GET.get('customemail','') # 取使用者Email
    if orderid == '' and customemail == '' :
        firstsearch = 1
    else :
        order = models.OrdersModel.objects.filter(id=orderid).first()
        if order == None or order.customemail != customemail :
            notfound = 1
        else:
            details = models.DetailModel.objects.filter(dorder=order)
    return render(request,"cartordercheck.html",locals()) 



