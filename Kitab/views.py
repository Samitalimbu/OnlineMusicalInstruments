from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django. contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from Kitab.models import Booking, kitab
from . import forms, models
from django.http import HttpResponseRedirect
from Kitab.forms import BookForm, KitabForm
from django.core.paginator import Paginator
from Kitab.forms import UserResgistrationForm

# For reset password

from django.core.mail import send_mail, BadHeaderError

from django.contrib.auth.forms import PasswordResetForm

from django.template.loader import render_to_string

from django.db.models.query_utils import Q

from django.utils.http import urlsafe_base64_encode

from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes

User=get_user_model()

# Create your views here.
def home(request):
    stores = kitab.objects.all
    return render(request, 'homepage.html', {'stores': stores})

@login_required(login_url='login')
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
    if request.method == 'POST':
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

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['Samitalimbu396@gmail.com'],  # To email
            # fail_silently= True,
        )
        return render(request, 'pages/contact.html', {'message_name': message_name})
    else:
        return render(request, 'pages/contact.html', {})


@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('admindashboard')
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')

# @login_required(login_url='login')


def admindashboard_view(request):
    user = get_user_model()
    usercount = user.objects.all().filter(is_superuser=False).count()
    bookingcount = Booking.objects.all().count()
    productcount = models.kitab.objects.all().count()

    order = Booking.objects.all()
    data = {
        'order': order,
        'usercount':usercount,
        'bookingcount':bookingcount,
        'productcount':productcount,
    }
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'adminControl/admindashboard.html', data)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')


@login_required(login_url='login')
def Kitab(request):
    if request.method == "POST":
        stores = KitabForm(request.POST, request.FILES)
        stores.save()
        return redirect("/store/kitab_pannel")
    else:

        stores = KitabForm()
    return render(request, 'adminControl/addData.html', {'stores': stores})


@login_required(login_url='login')
def admin_add_product_view(request):
    KitabForm = forms.KitabForm()
    if request.method == 'POST':
        KitabForm = forms.KitabForm(request.POST, request.FILES)
        if KitabForm.is_valid():
            KitabForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request, 'adminControl/addproduct.html', {'KitabForm': KitabForm})


def booking_pannel(request):
    stores = kitab.objects.raw('select * from Kitab')
    return render(request, "adminControl/buyNow.html", {'stores': stores})


@login_required(login_url='login')
def viewbooking_view(request):
    order = Booking.objects.all()
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'order': paged_product,
    }
    
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'adminControl/viewBooking.html', data)
    else:
        messages.error(request, "Invalid login credentials")
        return redirect('admin')

@login_required(login_url='login')
def viewcustomer(request):
    # user = User.objects.all()
    data = get_user_model()
    user = data.objects.all().filter(is_superuser=False)
    paginator = Paginator(user, 6)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    return render(request, 'adminControl/viewcustomer.html', {'user': paged_product})


# booking musical instruments

def buyNow(request, p_id):
    print(request)
    if request.method == "POST":
        form = BookForm(request.POST)
        try:
            form.save()
            messages.success(request, "your booking was done")
            return redirect('/')
        except:
            print("error")
    else:
        form = BookForm()
    kitabs = kitab.objects.get(kitab_id=p_id)
    return render(request, 'buyNow.html', {'kitabs': kitab, 'form': form})


# for booking hotel
@login_required(login_url='login')
def book_details(request, p_id):
    kitabs = kitab.objects.get(kitab_id=p_id)
    return render(request, 'adminControl/buyNow.html', {'kitabs': kitabs})


# @login_required(login_url='adminlogin')
# def view_customer(request):
#     User = get_user_model()
#     users=User.objects.all().order_by('username').filter(is_superuser=False)
#     paginator = Paginator(users, 2)
#     page = request.GET.get('page')
#     paged_product = paginator.get_page(page)
#     data = {
#         'users': paged_product,
#     }
#     return render(request,'admincontrol/view_customer.html',data)

@login_required(login_url='admin')
def admin_products_view(request):
    Kitab = models.kitab.objects.all()
    paginator = Paginator(Kitab, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    data = {
        'Kitab': paged_product,
    }

    return render(request, 'adminControl/admin_product.html', data)


def blog_detail(request):
    return render(request, 'pages/blog1.html')

def blog_detail2(request):
    return render(request, 'pages/blog2.html')

def blog_detail3(request):
    return render(request, 'pages/blog3.html')    

def blog_detail4(request):
    return render(request, 'pages/blog4.html')    



# @login_required(login_url='Hamro:login')
# def edit_profile_view(request):
#     user=User.objects.get(id=request.user.id)
#     userForm=forms.UserResgistrationForm(instance=user)
#     mydict={
#         'UserResgistrationForm':UserResgistrationForm,
#         'user':user
#     }
#     if request.method=='POST':
#         userForm=forms.UserResgistrationForm(request.POST, request.FILES, instance=user)
#         if userForm.is_valid():
#             user.set_password(user.password)
#             userForm.save()
#             # user.set_password(user.password)
#             # user.save()
#             return HttpResponseRedirect('dashboard')
#     return render(request,'pages/edit_profile.html',context=mydict)
def profile(request):
     return render(request, 'pages/profile.html')

@login_required(login_url='login')
def edit_profile_view(request):
    user=User.objects.get(id=request.user.id)
    userForm= forms.UserResgistrationForm(instance=user)
    mydict={
        'UserResgistrationForm':UserResgistrationForm,
        'user':user
    }
    if request.method=='POST':
        userForm=forms.UserResgistrationForm(request.POST, request.FILES, instance=user)
        if userForm.is_valid():
            user.set_password(user.password)
            userForm.save()
            # user.set_password(user.password)
            # user.save()
            return HttpResponseRedirect('/login')

    return render(request,'pages/edit_profile.html',context=mydict)    



def deleteproduct(request,p_id):
    user= kitab.objects.get(kitab_id = p_id)
    user.delete()
    return redirect("/admin-products")



def updateproduct(request,id):
    kitabs= kitab.objects.get(kitab_id = id)
    form = KitabForm(request.POST,instance=kitabs)
    if form.is_valid():
        form.save()
        print(form)
        return redirect('/admin-products')
      
        
    return render(request,'adminControl/editproducts.html',{'kitabs':kitabs})


def editproduct(request,id):
    kitabs = kitab.objects.get(kitab_id = id)
    return render(request,'adminControl/editproducts.html',{'kitabs':kitabs})




def Bdeleteproduct(request,p_id):
    user= Booking.objects.get(Mbooking_id = p_id)
    user.delete()
    return redirect("/viewbooking")    

def password_reset_request(request):

    if request.method == "POST":

        password_reset_form = PasswordResetForm(request.POST)

        if password_reset_form.is_valid():

            data = password_reset_form.cleaned_data['email']

            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():
                for user in associated_users:

                    subject = "Password Reset Requested"

                    email_template_name = "pages/password_reset_email.txt"

                    c = {

                    "email":user.email,

                    'domain':'127.0.0.1:8000',

                    'site_name': 'Website',

                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),

                    "user": user,

                    'token': default_token_generator.make_token(user),

                    'protocol': 'http',

                    }

                    email = render_to_string(email_template_name, c)

                    try:

                        send_mail(subject, email, 'samitalimbu396@gmail.com' , [user.email], fail_silently=False)

                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    return redirect ("/password_reset/done/")

    password_reset_form = PasswordResetForm()

    return render(request=request, template_name="pages/password_reset_form.html", context={"password_reset_form":password_reset_form})
