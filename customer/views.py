from django.shortcuts import render,redirect
from . models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def cuhome (request):
    
    if request.method == "POST" :
        mail = request.POST['c_email']
        message = request.POST['c_message']
        contactform = Contactmessage (contact_email = mail , contact_message = message)
        contactform.save()
        return render (request, "customer/cuhome.html" , {'msg' : 'we will get back to you as soon as possible'})
    return render (request,'customer/cuhome.html')


  
def register1 (request):
    return render (request,'customer/register1.html')   

def signin (request):
    if request.method == "POST" :
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mob = request.POST['mob']
        city = request.POST['city']
        state = request.POST['state']
        crtpswd = request.POST['pswd1']
        pswd = request.POST['pswd2']
        customer_exist = Registrationcustomer.objects.filter(email=email).exists()
        if not customer_exist :
            otp = randint(1000,9999)
            send_mail(
                'please verify your otp',
                str(otp),
                settings.EMAIL_HOST_USER,
                [email]
            )
        regc = Registrationcustomer(fname=fname, lname=lname, email=email, city=city, mob=mob, state=state, otp=otp, crtepswd=crtpswd, pswd=pswd)
        
        regc.save()
        customer = Registrationcustomer.objects.get(email=email)
        request.session['customerid']=customer.id
        return redirect('customer:cust_otp_n')
        return render (request,'customer/login.html')
    return render (request,'customer/sign.html')    

def userpage (request):
    return render (request,'customer/user.html')    

def userinpage (request):
    return render (request,'customer/userin.html')    


def vrest (request):
    return render (request,'customer/restaurent.html')    

def vdeliciaRest (request):
    return render (request,'customer/deliciaRest.html')
def otpverification(request):
    return render(request,'customer/verifyotp.html')
def login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        customer_exist = Registrationcustomer.objects.filter(email=email,pswd=password).exists()
        if customer_exist :
            customer = Registrationcustomer.objects.get(email=email,pswd=password)
            request.session['customerid']=customer.id
            if customer.status == 'toverify':
                otp = randint(1000,9999)
                send_mail(
                'please verify your otp',
                str(otp),
                settings.EMAIL_HOST_USER,
                [customer.customer_mail]
                )
                customer.otp=otp
                customer.save()
                return redirect('customer:cust_otp_n')
            else :
                return redirect('customer:userinpg')
        else :
                return render(request, 'customer/login.html', {'msg':'invalid username/password'})
    
    return render(request,'customer/login.html')
def cust_otp_v(request):
    if request.method == 'POST' :
        otp = request.POST['otp']
        c_id = request.session['customerid']
        customer =Registrationcustomer.objects.get(id=c_id)
        if otp==customer.otp :
            Registrationcustomer.objects.filter(id=c_id).update(status='verified')
            return redirect('customer:userinpg')
        else :
            return render (request,'customer/otp.html' ,{'msg':'invalid otp'})
    return render(request, 'customer/otp.html')
def customerdetails(request):
    customers = Registrationcustomer.objects.all()
    return render(request,'customer/customerdetails.html',{'cust':customers})


def cust_update_v(request,customerid):
    # if request.method =='POST':
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     mob = request.POST['mob']
    #     city = request.POST['city']
    #     state = request.POST['state']
    #     crtpswd = request.POST['pswd1']
    #     pswd = request.POST['pswd2']
        
    #     Registrationcustomer.objects.filter(id=customerid).update(fname=fname ,lname=lname, email=email, mob=mob, city=city,state=state,crtepswd=crtpswd,pswd=pswd)
    #     return redirect('customer:login')
    # updatecust = Registrationcustomer.objects.get(id=customerid)
    return render (request,'customer/mpcustomer.html') 
    
def delete_customer_v(request,customerid):
    Registrationcustomer.objects.get(id=customerid).delete()
    return redirect('customer:customerdetail_n')    
def checkemailuser(request):
    mailid = request.POST['email']
    user = Registrationcustomer.objects.filter(email=mailid).exists()
    if user :
        return JsonResponse({
            'is_available' : False
        })
    else :
        return JsonResponse({
            'is_available' : True
        })
           
def hotels(request):
    return render(request,'customer/hotel.html')
def plslogin(request):
    return render(request,'customer/loginpls.html')
def photographer(request):
    return render(request,'customer/photographer.html')
def driver(request):
    return render(request,'customer/driver.html')
def guide(request):
    return render(request,'customer/guide.html')




    