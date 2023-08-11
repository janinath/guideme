from django.shortcuts import render,redirect
from . models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def mehome (request):
    return render (request,'member/mehome.html')
def guidereg (request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mob = request.POST['mob']
        gender = request.POST['gender']
        propic = request.POST['propic']
        idtype = request.POST['idtype']
        idnum = request.POST['idnum']
        idimg = request.POST['idimg']
        sidtype = request.POST['sidtype']
        sidnum = request.POST['sidnum']
        sidimg = request.POST['sidming']
        natn = request.POST['natn']
        state = request.POST['state']
        dist = request.POST['dist']
        street = request.POST['street']
        post = request.POST['post']
        pin = request.POST['pin']
        place = request.POST['place']
        time = request.POST['time']
        wapp = request.POST['wapp']
        amount = request.POST['amount']
        user = request.POST['user']
        cuser = request.POST['cuser']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        guideregform = Guideregistration(full_name=fullname,date_of_birth=dob,e_mail=email,mobile_number=mob,gender=gender,profile_photo=propic,id_type=idtype,id_number=idnum,image_of_id=idimg,second_id_type=sidtype,second_id_number=sidnum,second_image_of_id=sidimg,nationality=natn,state=state,district=dist,street_name=street,post=post,pin_code=pin,wapp_number=wapp,available_place=place,available_time=time,amount_hours=amount,username=user,confirm_username=cuser,password=pswd,confirm_password=cpswd,status="waiting")
        guideregform.save()
    return render (request, 'member/guidereg.html')
def hotelreg (request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mob = request.POST['mob']
        gender = request.POST['gender']
        propic = request.POST['propic']
        idtype = request.POST['idtype']
        idnum = request.POST['idnum']
        idimg = request.POST['idimg']
        sidtype = request.POST['sidtype']
        sidnum = request.POST['sidnum']
        sidimg = request.POST['sidimg']
        natn = request.POST['natn']
        state = request.POST['state']
        dist = request.POST['dist']
        street = request.POST['street']
        post = request.POST['post']
        pin = request.POST['pin']
        hotname = request.POST['hotname']
        hotad = request.POST['hotad']
        license = request.POST['license']
        photo = request.POST['photo']
        wapp = request.POST['wapp']
        time = request.POST['time']
        user = request.POST['user']
        cuser = request.POST['cuser']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        hotelregform = Hotelregistration(full_name=fullname,date_of_birth=dob,e_mail=email,mobile_number=mob,gender=gender,profile_photo=propic,id_type=idtype,id_number=idnum,image_of_id=idimg,second_id_type=sidtype,second_id_number=sidnum,second_image_of_id=sidimg,nationality=natn,state=state,district=dist,street_name=street,post=post,pin_code=pin,wapp_number=wapp,photos=photo,hotel_name=hotname,hotel_address=hotad,license_photo=license,working_hours=time ,username=user,confirm_username=cuser,password=pswd,confirm_password=cpswd,status='waiting')
        hotelregform.save()
        return redirect('member:loginhot')
    return render (request, 'member/hotelreg.html')
def restaurentreg (request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mob = request.POST['mob']
        gender = request.POST['gender']
        propic = request.POST['propic']
        idtype = request.POST['idtype']
        idnum = request.POST['idnum']
        idimg = request.POST['idimg']
        resname = request.POST['resname']
        resad = request.POST['resad']
        license = request.POST['license']
        photo = request.POST['photo']
        wapp = request.POST['wapp']
        time = request.POST['time']
        user = request.POST['user']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        restegform = Restaurentregistration(full_name=fullname,date_of_birth=dob,e_mail=email,mobile_number=mob,gender=gender,profile_photo=propic,id_type=idtype,id_number=idnum,image_of_id=idimg,wapp_number=wapp,photos=photo,rest_name=resname,rest_address=resad,license_number=license,working_hours=time ,username=user,password=pswd,confirm_password=cpswd,status='waiting')
        restegform.save()
        return redirect('member:memlogin')
    return render (request, 'member/restaurentreg.html',)
def photographerreg (request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mob = request.POST['mob']
        gender = request.POST['gender']
        propic = request.POST['propic']
        idtype = request.POST['idtype']
        idnum = request.POST['idnum']
        idimg = request.POST['idimg']
        sidtype = request.POST['sidtype']
        sidnum = request.POST['sidnum']
        sidimg = request.POST['sidimg']
        natn = request.POST['natn']
        state = request.POST['state']
        dist = request.POST['dist']
        street = request.POST['street']
        post = request.POST['post']
        pin = request.POST['pin']
        place = request.POST['place']
        time = request.POST['time']
        photo = request.POST['photo']
        wapp = request.POST['wapp']
        studio = request.POST['studio']
        amount = request.POST['amount']
        user = request.POST['user']
        cuser = request.POST['cuser']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        photoregform = Photographerregistration(full_name=fullname,date_of_birth=dob,e_mail=email,mobile_number=mob,gender=gender,profile_photo=propic,id_type=idtype,id_number=idnum,image_of_id=idimg,second_id_type=sidtype,second_id_number=sidnum,second_image_of_id=sidimg,nationality=natn,state=state,district=dist,street_name=street,post=post,pin_code=pin,wapp_number=wapp,photos=photo,available_place=place,available_time=time,studio_name=studio,amount_hours=amount,username=user,confirm_username=cuser,password=pswd,confirm_password=cpswd,status='waiting')
        photoregform.save()
        return redirect ('member:nphlogin')
    return render (request, 'member/photoreg.html')
def driverreg (request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mob = request.POST['mob']
        gender = request.POST['gender']
        propic = request.POST['propic']
        idtype = request.POST['idtype']
        idnum = request.POST['idnum']
        idimg = request.POST['idimg']
        sidtype = request.POST['sidtype']
        sidnum = request.POST['sidnum']
        sidimg = request.POST['sidimg']
        natn = request.POST['natn']
        state = request.POST['state']
        dist = request.POST['dist']
        street = request.POST['street']
        post = request.POST['post']
        pin = request.POST['pin']
        place = request.POST['place']
        time = request.POST['time']
        license = request.POST['license']
        wapp = request.POST['wapp']
        model = request.POST['model']
        rc = request.POST['rc']
        user = request.POST['user']
        cuser = request.POST['cuser']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        driverregform = Driverregistration(full_name=fullname,date_of_birth=dob,e_mail=email,mobile_number=mob,gender=gender,profile_photo=propic,id_type=idtype,id_number=idnum,image_of_id=idimg,second_id_type=sidtype,second_id_number=sidnum,second_image_of_id=sidimg,nationality=natn,state=state,district=dist,street_name=street,post=post,pin_code=pin,wapp_number=wapp,license=license,available_place=place,available_time=time,rc=rc,vehicle_model=model,username=user,confirm_username=cuser,password=pswd,confirm_password=cpswd)
        driverregform.save()
    return render (request, 'member/driverreg.html')

def rest_mem_details(request):
    rest_members=Restaurentregistration.objects.filter(status='waiting')
    return render(request,'member/restmem.html' ,{'rest_mem':rest_members})
def ph_mem_details(request):
    ph_members=Photographerregistration.objects.filter(status='waiting')
    return render(request,'member/phmem.html' ,{'ph_mem':ph_members})
def ho_mem_details(request):
    ho_members=Hotelregistration.objects.filter(status='waiting')
    return render(request,'member/homem.html',{'ho_mem':ho_members})

def delete_rest_mem(request,restid):
    Restaurentregistration.objects.get(id=restid).delete()
    return redirect('member:nrestmem')
def delete_ph_mem(request,phid):
    Photographerregistration.objects.get(id=phid).delete()
def delete_ho_mem(request,hoid):
    Hotelregistration.objects.get(id=hoid).delete()    
    return redirect('member:nphmem')

def accept_rest_mem(request,restid):
    Restaurentregistration.objects.filter(id=restid).update(status='active')
    return redirect('member:waitinglist')
def ph_mem_accept(request,phid):
    Photographerregistration.objects.filter(id=phid).update(status='active')
    return redirect('member:waitinglist')
def ho_mem_accept(request,hoid):
    Hotelregistration.objects.filter(id=hoid).update(status='active')
    return redirect('member:waitinglist')
def dr_mem_accept(request,drid):
    Driverregistration.objects.filter(id=drid).update(status='active')
    return redirect('member:waitinglist')

def login_driver(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member_exist = Driverregistration.objects.filter(username=username,password=password).exists()
        if member_exist :
            member = Driverregistration.objects.get(username=username,password=password)
            request.session['memberid']=member.id
            if member.status == 'waiting' :
                return redirect('member:waiting')
            else :
                return redirect('member:resdashboard')
    return render(request, 'member/login.html')
def login_guide(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member_exist = Guideregistration.objects.filter(username=username,password=password).exists()
        if member_exist :
            member = Guideregistration.objects.get(username=username,password=password)
            request.session['memberid']=member.id
            if member.status == 'waiting' :
                return redirect('member:waiting')
            else :
                return redirect('member:resdashboard')
    return render(request, 'member/login.html')
def login_hotel(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member_exist = Hotelregistration.objects.filter(username=username,password=password).exists()
        if member_exist :
            member = Hotelregistration.objects.get(username=username,password=password)
            request.session['memberid']=member.id
            if member.status == 'waiting' :
                return redirect('member:waiting')
            else :
                return redirect('member:resdashboard')
    return render(request, 'member/login.html')
def login_mem(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member_exist = Restaurentregistration.objects.filter(username=username,password=password).exists()
        if member_exist :
            member = Restaurentregistration.objects.get(username=username,password=password)
            request.session['memberid']=member.id
            if member.status == 'waiting' :
                return redirect('member:waiting')
            else :
                return redirect('member:resdashboard')
    return render(request, 'member/login.html')
def phlogin (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        member_exist = Photographerregistration.objects.filter(username=username,password=password).exists()
        if member_exist :
            member = Photographerregistration.objects.get(username=username,password=password)
            request.session['memberid']=member.id
            if member.status == 'waiting' :
                return redirect('member:waiting')
            else :
                return redirect('member:phdashboard')
    return render (request, 'member/phlogin.html')

    

def res_dashboard(request):
    return render(request,'member/resdashboard.html')
def ph_dashboard(request):
    return render (request, 'member/phdashboard.html')




def ph_mem_reject(request,phid):
    ph_rej_mem = Photographerregistration.objects.filter(id=phid).update(status='rejected')
    return redirect('member:waitinglist')
def ho_mem_reject(request,hoid):
    Hotelregistration.objects.filter(id=hoid).update(status='rejected')
    return redirect('member:waitinglist')
def rest_mem_reject(request,rrid):
    Restaurentregistration.objects.filter(id=rrid).update(status='rejected')
    return redirect('member:waitinglist')
def dr_mem_reject(request,drid):
    Driverregistration.objects.filter(id=drid).update(status='rejected')
    return redirect('member:waitinglist')



def accept (request):
    res_acc_mem = Restaurentregistration.objects.filter(status='active')
    ho_members=Hotelregistration.objects.filter(status='active')
    ph_members=Photographerregistration.objects.filter(status='active')

    return render(request, 'member/accepted.html',{'active':res_acc_mem,'ho_mem':ho_members,'ph_mem':ph_members})
def reject (request):
    res_rej_mem = Restaurentregistration.objects.filter(status='rejected')
    ph_members=Photographerregistration.objects.filter(status='rejected')
    ho_members=Hotelregistration.objects.filter(status='waiting')
    return render(request, 'member/rejected.html',{'reject':res_rej_mem,
                                                   'ph_mem':ph_members,
                                                   'ho_mem':ho_members})
def waiting(request):
    return render (request, 'member/waiting.html')
def waiting_list(request):
    res_acc_mem = Restaurentregistration.objects.filter(status='waiting')
    ho_members=Hotelregistration.objects.filter(status='waiting')
    ph_members=Photographerregistration.objects.filter(status='waiting')
    return render(request,'member/waitinglist.html',{'rest_mem':res_acc_mem,'ho_mem':ho_members,'ph_mem':ph_members})

