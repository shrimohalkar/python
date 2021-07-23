from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from userapp.models import signup
from .models import categorys,subcategorys,Product

# Create your views here.

def login(request):
    return render(request,'page-login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('/')

def adminlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            vusername=request.POST.get('username')
            vpasswaord=request.POST.get('password')
            user=auth.authenticate(username=vusername,password=vpasswaord)
            if user is not None:
                auth.login(request,user) # login is predefined function
                return redirect('dashboard')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('/')
        else:
            return render(request,'/')
    else:
        return render(request,'page-login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def category(request):
    if request.user.is_authenticated:
        cat=categorys.objects.all()
        return render(request,'category.html',{'cat':cat})
    else:
        return redirect('/')

def product(request):
    if request.user.is_authenticated:
        prod=Product.objects.raw("select * from adminapp_product left join adminapp_categorys on adminapp_product.category_ID=adminapp_categorys.id left join adminapp_subcategorys on adminapp_product.Subcategory_ID=adminapp_subcategorys.id")
        return render(request,'product.html',{'prod':prod})
    else:
        return redirect('/')

def manage_user(request):
    if request.user.is_authenticated:
        userd=signup.objects.all
        return render(request, 'manage_user.html',{'userd':userd})
    else:
        return redirect('/')

def delete_manage_user(request,eid):
    userd=signup.objects.get(id=eid)
    userd.delete()
    return redirect('manage_user')

def userstatus(request,eid,status):
    if(status=="BLOCK"):
        userd = signup.objects.get(id=eid)
        userd.status="UNBLOCK"
        userd.save()
        return redirect('/manage_user')
    else:
        userd = signup.objects.get(id=eid)
        userd.status="BLOCK"
        userd.save()
        return redirect('/manage_user')

def insertproduct(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            catname=request.POST.get('cate')
            subcat=request.POST.get('subcate')
            prod_name = request.POST.get('product_name')
            prod_price = request.POST.get('product_price')
            prod_discount = request.POST.get('discount')
            discount_price = request.POST.get('discount_price')
            img=request.FILES['image']
            descreption=request.POST.get('descreption')
            prod=Product()
            prod.category_ID=catname
            prod.Subcategory_ID=subcat
            prod.product_name=prod_name
            prod.product_price=prod_price
            prod.Discount=prod_discount
            prod.Discount_price=discount_price
            prod.image=img
            prod.Descreption=descreption
            prod.save()
            return redirect('/product')
        else:
            return render(request, 'add_product.html')
    else:
        return redirect('/')


def updateproduct(request,eid):
            prod=Product.objects.get(id=eid)
            pcatname=request.POST.get('cate')
            psubcat=request.POST.get('subcate')
            pprod_name = request.POST.get('product_name')
            pprod_price = request.POST.get('product_price')
            pprod_discount = request.POST.get('discount')
            pdiscount_price = request.POST.get('discount_price')
            pdescreption = request.POST.get('descreption')

            if request.POST.get('image'==''):
                prod.image=prod.image
            else:
                prod.image=request.FILES['image']


            prod.category_ID=pcatname
            prod.Subcategory_ID=psubcat
            prod.product_name=pprod_name
            prod.product_price=pprod_price
            prod.Discount=pprod_discount
            prod.Discount_price=pdiscount_price
            prod.Descreption=pdescreption
            prod.save()
            return redirect('/product')

def addproduct(request):
    if request.user.is_authenticated:
        cat = categorys.objects.all()
        subcat=subcategorys.objects.raw("select * from adminapp_subcategorys left join adminapp_categorys on adminapp_subcategorys.category=adminapp_categorys.id;")
        return render(request, 'add_product.html', {'cat': cat,'subcat':subcat})
    else:
        return redirect('/')

def addcategory(request):
    if request.user.is_authenticated:
        cat = categorys.objects.all()
        return render(request,'addcategory.html',{'cat':cat})
    else:
        return redirect('/')

def insertrecord(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            cname=request.POST.get('category')
            cat = categorys()
            cat.category_name=cname
            cat.save()
            return redirect('/category')
        else:
            return render(request, 'addcategory.html')
    else:
        return redirect('/')

def subcategory(request):
    if request.user.is_authenticated:
        cat=subcategorys.objects.raw("select * from adminapp_subcategorys left join adminapp_categorys on adminapp_subcategorys.category=adminapp_categorys.id")
        return render(request,'subcategory.html',{'cat':cat})
    else:
        return redirect('/')

def addsubcategory(request):
    if request.user.is_authenticated:
        cat = categorys.objects.all()
        return render(request, 'addsubcategory.html', {'cat': cat})
    else:
        return redirect('/')

def insertsubcat(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            ccat=request.POST.get('cate')
            cname=request.POST.get('subcategory')
            cat = subcategorys()
            cat.subcategory_name=cname
            cat.category=ccat
            cat.save()
            return redirect('/subcategory')
        else:
            return render(request,'addsubcategory.html')
    else:
        return redirect('/')

def deleterecord(request,eid):
    cat=categorys.objects.get(id=eid)
    cat.delete()
    return redirect('category')

def deletesubcat(request,eid):
    subcat=subcategorys.objects.get(id=eid)
    subcat.delete()
    return redirect('/subcategory')

def deleteproduct(request,eid):
    prod=Product.objects.get(id=eid)
    prod.delete()
    return redirect('/product')

def editcategory(request,eid): # fetch the value in text box
    cat=categorys.objects.get(id=eid)
    return render(request,'editcategory.html',{'cat':cat})

def editsubcat(request,eid): # fetch the value in text box
    cat=categorys.objects.all()
    subcat=subcategorys.objects.get(id=eid)
    return render(request,'editsubcategory.html',{'cat':cat,'subcat':subcat})

def editproduct(request,eid): # fetch the value in text box
    prod=Product.objects.get(id=eid)
    cat = categorys.objects.all()
    subcat = subcategorys.objects.all()
    return render(request,'editproduct.html',{'prod':prod,'cat':cat,'subcat':subcat})

def updatecategory(request,eid):
    if request.user.is_authenticated:
        cat = categorys.objects.get(id=eid)
        cname=request.POST.get('category')
        cat.category_name=cname
        cat.save()
        return redirect('category')
    else:
        return redirect('/')

def updatesubcategory(request,eid):
    if request.user.is_authenticated:
        scat = subcategorys.objects.get(id=eid)
        ccat=request.POST.get('cate')
        cname=request.POST.get('subcategory')
        scat.subcategory_name=cname
        scat.category=ccat
        scat.save()
        return redirect('/subcategory')
    else:
        return redirect('/')


def categorystatus(request,eid,status):
    if(status=="BLOCK"):
        cat=categorys.objects.get(id=eid)
        cat.status="UNBLOCK"
        cat.save()
        return redirect('/category')
    else:
        cat=categorys.objects.get(id=eid)
        cat.status="BLOCK"
        cat.save()
        return redirect('/category')

def subcategorystatus(request,eid,status):
    if(status=="BLOCK"):
        cat= subcategorys.objects.get(id=eid)
        cat.status="UNBLOCK"
        cat.save()
        return redirect('/subcategory')
    else:
        cat=subcategorys.objects.get(id=eid)
        cat.status="BLOCK"
        cat.save()
        return redirect('/subcategory')

def productstatus(request,eid,status):
    if(status=="BLOCK"):
        prod=Product.objects.get(id=eid)
        prod.status="UNBLOCK"
        prod.save()
        return redirect('/product')
    else:
        prod=Product.objects.get(id=eid)
        prod.status="BLOCK"
        prod.save()
        return redirect('/product')



def getsubcategory(request):
    cat=request.GET.get('category')
    subcat=subcategorys.objects.filter(category=cat)
    print(subcat)
    return render(request,'getsubcategory.html',{'subcat':subcat})