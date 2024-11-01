from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import View
from .forms import StudentInformationForm,ProductForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.shortcuts import get_object_or_404

def index(request):
    banner = Banner.objects.all()
    product = Product.objects.all()
    return render(request, 'index.html',{"banner":banner,'product':product})

# class About(View):
#     def get(self, request):
#         return HttpResponse("Hi good mornging") 

def about(request):
    return render(request,'practice/about.html')


def student_information(request):
    # if request.method == "POST":
    #     form = StudentInformationForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         id = form.cleaned_data['id']
    #         email = form.cleaned_data['email']
    #         subject = form.cleaned_data['subject']

            
    #         print("first_name =======", first_name)
    #         print("last_name =======", last_name)
    #         print("id =======", id)
    #         print("email =======", email)
    #         print("subject =======", subject)

    #         return redirect('home')
    # else: 
    #     form = StudentInformationForm()


    if request.method == "POST":
        form = StudentInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentInformationForm()     
    return render(request, "student.html",{"form":form})  

  

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm() 
    return render(request, 'product.html', {'form':form})      

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()    

    return render(request, 'user/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        
        if user is not None: 
            login(request,user)
            return redirect('home')
   
    return render(request, 'user/login.html')        

def passwordchange(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request,'user/change_password.html', {'form': form})        


def product_create2(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form':form}) 

def product_update(request,pk):
    p = get_object_or_404(Product,id=pk)
    form = ProductForm(request.POST, request.FILES, instance=p)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product.html', {'form':form})

def product_delete(request,pk):
    p = get_object_or_404(Product,pk=pk)
    p.delete()
    return redirect('home')
    

def product_details(request,id):
    p = get_object_or_404(Product,id=id)
    return render(request, 'product-details.html', {'p':p})

def product_details(request, slug):
    p = get_object_or_404(Product,slug=slug)

    return render(request, 'product-details.html', {'p':p})


def category(request):
    query = Category.objects.all()

    return render(request,'category.html',{'query':query})

