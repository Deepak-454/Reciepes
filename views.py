from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        name=data.get("receipe_name")
        receipe=data.get("receipe_description")
        Receipes.objects.create(receipe_name=name,
                                receipe_description=receipe,
                                receipe_image=receipe_image)
        return redirect('/receipes/')
    queryset=Receipes.objects.all()
    if 'search' in request.GET and 'filter' in request.GET:
        def s(a):
            if a =="":
                return "receipe_name__icontains"
            if a == "description":
                return "receipe_description__icontains" 
            else:
                return None
        filter=s(request.GET.get('filter'))  
        search=request.GET.get('search')
        if filter:
            queryset=Receipes.objects.filter(**{filter:search}) 
        else:
            queryset=Receipes.objects.all()          
    return render(request,"receipe.html",context={"receipes":queryset})
def delete_receipe(request,id):
    Receipes.objects.get(id=id).delete()
    return redirect("/receipes/")
def update_receipe(request,id):
    queryset=Receipes.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        name=data.get("receipe_name")
        receipe=data.get("receipe_description")
        Receipes.objects.filter(id=id).update(receipe_name=name,
                                receipe_description=receipe)
        if receipe_image:
            queryset.receipe_image=receipe_image
            queryset.save()
        return redirect('/receipes/')
    return render(request,'update.html',context={'update':queryset})
def login_page(request):
    if request.method=="POST":
        user=request.POST.get("username")
        password=request.POST.get("password")
        if not User.objects.filter(username=user).exists():
            print("error")
            messages.info(request,"Username invalid")  
            return redirect('/login/')
        else:
            user=authenticate(username=user,password=password)
            if user==None:
                messages.info(request,"Invalid Password")
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('/receipes/')    
    return render(request,"login.html")
def logout_page(request):
    logout(request)
    return redirect('/login/')
def register(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get("firstname")
        last_name=data.get("lastname")
        username=data.get("username")
        password=data.get("password")
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already taken")
            return redirect("/Register/")
        else:
            user=User.objects.create(first_name=first_name,
                                     last_name=last_name,
                                     username=username)
            user.set_password(password)
            user.save()
            messages.info(request,"Registered")
            return redirect("/login/")
    return render(request,"register.html")
