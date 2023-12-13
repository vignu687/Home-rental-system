import os
from django.shortcuts import render,redirect,get_object_or_404
from .form import Captchaform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import Houses,Result
from django.db.models import Q
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
       return render(request,'index.html')

def mainn(request):
    items=Houses.objects.filter(issold=False)
    context={
        'items':items
    }
    return render(request,'main.html',context)
@csrf_protect
def loginuser(request):
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('pass')

            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('mainn')
            else:
                return redirect('loginuser')
    else:
        return render(request,'login.html')
@csrf_protect   
def signupuser(request):
    if request.method=="POST":
        form=Captchaform(request.POST)
        if form.is_valid():
            username=request.POST.get('username') 
            email=request.POST.get('email')
            password=request.POST.get('pass')

            if User.objects.filter(username=username).exists():
                messages.info(request,'Already exists')
                return redirect('signupuser')
            elif User.objects.filter(email=email):
                messages.info(request,'Already exists')
                return redirect('signupuser')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('loginuser')
    else:
        form=Captchaform()
    return render(request,'register.html',{'form':form})
            

def logoutuser(request):
    logout(request)
    return redirect('index')


def detail(request, pk):
    item = get_object_or_404(Houses, pk=pk)
    return render(request, 'detail.html', {'item': item})

def sold(request,pk):
        item = get_object_or_404(Houses, pk=pk)
        productbuyer=request.user
        powner=item.createdby
        result=Result()
        result.probuyer=productbuyer
        result.proowner=powner
        result.save()
        item.issold=True
        item.save()
        return redirect('mainn')


def search(request):
    query = request.GET.get('query', '')
    items = Houses.objects.filter(issold=False)

    if query:
       items = items.filter(Q(address__icontains=query) | Q(housetype__icontains=query) | Q(state__icontains=query))

    return render(request, 'search.html', {'items': items, 'query': query})

@login_required
def sell(request):
    if request.method == "POST":
        user=request.user
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        country = request.POST.get('country')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        price = request.POST.get('price')
        htype = request.POST.get('htype')
        htitle = request.POST.get('title')


        contact = request.POST.get('contact')
        desp = request.POST.get('desp')
        house=Houses()
        house.image1 = image1
        house.image2 = image2
        house.image3 = image3
        house.housename=htitle
        house.country = country
        house.state = state
        house.housetype=htype
        house.district = district
        house.address = address
        house.price = price
        house.contact = contact
        house.desp = desp
        house.createdby=user
        house.save()
        return redirect('mainn')

   
    return render(request, 'sell.html')


def sendmainn(request):
    return redirect('mainn')


def bought(request):
    item = Houses.objects.filter(createdby=request.user, issold=True)
    info = Result.objects.filter(proowner=request.user)

    zipped_data = zip(item, info)

    return render(request,'result.html',{'zipped_data':zipped_data})