from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django. contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from Kitab.models import Booking, kitab
from . import forms, models
from django.http import HttpResponseRedirect,HttpResponse
from Kitab.forms import BookForm, KitabForm

# Create your views here.
def home(request):
    stores=kitab.objects.all
    return render(request, 'homepage.html',{'stores':stores})



def aboutus(request):
    return render(request, 'pages/aboutus.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'pages/dashboard.html')



def adminlogin(request):
    return render(request, 'adminControl/adminlogin.html')    








def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")      
            return redirect('login')
    return render(request, 'pages/login.html')  


def register(request):



    if request.method =='POST':

        username = request.POST.get('username')

        first_name = request.POST.get('first_name')

        email = request.POST.get('email')

        password = request.POST.get('password')

        user = User.objects.create_user(

                            username=username,

                            email=email,

                            first_name=first_name,

                            password=password)

        user.save()

        print("here")

        return redirect('/login')

    else:

        return render(request, 'pages/register.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'pages/dashboard.html')        



def logout(request):

    if request.method == 'POST':

        auth.logout(request)

        # messages.success(request, 'You are successfully logged out.')

        return redirect('login')

    return redirect('home')




def contact(request):

    if request.method == "POST":

        message_name = request.POST['message_name']

        message_email = request.POST['message_email']

        message =request.POST['message']



        send_mail(

            message_name, #subject

            message, #message

            message_email, #from email

          

            ['Samitalimbu396@gmail.com' ], #To email

            # fail_silently= True,

        )  

        return render(request, 'pages/contact.html', {'message_name': message_name})



    else:

        return render(request, 'pages/contact.html' , {}) 


@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('admindashboard')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')

@login_required(login_url='login')
def admindashboard_view(request):
    order=Booking.objects.all()
    data={
        'order':order,
    }
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'adminControl/admindashboard.html',data)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')




@login_required(login_url='login')
def Kitab(request):
    if request.method=="POST":
        stores=KitabForm(request.POST,request.FILES)
        stores.save()
        return redirect ("/store/kitab_pannel")
    else:

        stores=KitabForm()
    return render(request, 'adminControl/addData.html',{'stores':stores})  



@login_required(login_url='login')
def admin_add_product_view(request):
    KitabForm=forms.KitabForm()
    if request.method=='POST':
        KitabForm=forms.KitabForm(request.POST, request.FILES)
        if KitabForm.is_valid():
            KitabForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request,'adminControl/addproduct.html',{'KitabForm':KitabForm})    



def booking_pannel(request):
 stores=kitab.objects.raw('select * from Kitab')
 return render(request,"adminControl/buyNow.html",{'stores':stores})    




#booking musical instruments

def buyNow(request,p_id):
    print(request)
    if request.method=="POST":
        form=BookForm(request.POST)
        try:
            form.save()
            messages.success(request,"your booking was done")
            return redirect('/kitab')
        except:
            print("error")
    else:
        form=BookForm()
    kitabs=kitab.objects.get(kitab_id=p_id)
    return render(request,'buyNow.html',{'kitabs':kitab,'form':form})   


#for booking hotel

def book_details(request,p_id):

    kitabs=kitab.objects.get(kitab_id=p_id)

    return render(request,'adminControl/buyNow.html',{'kitabs':kitabs})      


@login_required(login_url='admin')
def admin_products_view(request):
    Kitab=models.kitab.objects.all()
    return render(request,'adminControl/admin_product.html',{'kitab':Kitab})    



   