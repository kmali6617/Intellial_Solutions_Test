from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from testapp.models import Customer_details,Order,Product_details
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render,HttpResponse,HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        q = request.POST.get('q')
        data=Order.objects.filter(first_name=q,pname=q)
    else:
        data = Order.objects.all()
        print (data)
    return render(request,"home.html",{'data':data})

def Order(request):
    if request.method == 'POST':
        Qty = request.POST.get('qty')

    data = Order.objects.all()
    for i in data:
        first_name=i.Customer_details.first_name
        Pname=i.Product_details.Pname
        Unit_price=i.Product_details.Unit_price(Product_details.Pname)
    print (data)
    print (first_name)
    print (Pname)
    print (Unit_price)
   
    Total_price = Qty * Unit_price
    obj = Order()
    obj.Qty= Qty
    obj.Total_price =Total_price
    
    return render(request,"Order.html",{'data':data,'cname':first_name,'pname':Pname,'Price':Unit_price,'Total_price':Total_price})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        first_name = request.POST.get('first_name')
        Pname = request.POST.get('Pname')
        Qty = request.POST.get('qty')
        Unit_price=request.POST.get('Unit_price')
        Total_price = Qty * Unit_price

        obj=Order() 
        obj.Customer_details.first_name=first_name
        obj.Product_details.Pname=Pname
        obj.Product_details.Unit_price=Unit_price
        obj=Qty
        obj=Total_price
        obj.save()

        msg="Data Stored Successfully"
        return render(request,"home.html",{'msg':msg})
  

def edit(request):
    ID = request.GET['id']
    for data in Order.objects.filter(ID=ID):
        first_name=data.Customer_details.first_name
        Pname=data.Product_details.Pname
        Unit_price=data.Product_details.Unit_price(Product_details.name)
        Qty=data.Qty
        Total_price=data.Total_price
    return render(request,"edit.html",{'ID':ID,'canme':first_name,'pname':Pname,'Price':Unit_price,'Total_price':Total_price})


def delete(request):
    ID = request.GET['id']
    Order.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("home")

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        first_name = request.POST.get('first_name')
        Pname = request.POST.get('Pname')
        Qty = request.POST.get('qty')
        Unit_price=request.POST.get('Unit_price')
        Total_price = Qty * Unit_price
        Order.objects.filter(ID=ID).update(first_name=first_name, Pname=Pname, Qty=Qty, Unit_price=Unit_price, Total_price=Total_price)
        obj = Order.objects.filter(ID=ID)
        return HttpResponseRedirect("home")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")