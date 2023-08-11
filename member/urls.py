from django.urls import path
from.import views
app_name='member'


urlpatterns=[
    path('',views.mehome, name="nmehome"),
    path('guidereg', views.guidereg, name="nguidereg" ),
    path('hotelsreg',views.hotelreg, name="nhotelreg"),
    path('restaurentreg',views.restaurentreg, name="nrestaurentreg"),
    path('photographerreg',views.photographerreg, name="nphotographerreg"),
    path('driverreg',views.driverreg, name="ndriverreg"),
    
    path('memlogin/',views.login_mem,name='memlogin'),
    path('logindri/',views.login_driver , name="logindri"),
    path('logingui',views.login_guide , name="logingui"),
    path('loginhot',views.login_hotel , name="loginhot"),
    path('phlogin/',views.phlogin, name="nphlogin"),

    path('restm/',views.rest_mem_details,name='nrestmem'),
    path('phm/',views.ph_mem_details,name='nphmem'),
    path('homem/',views.ho_mem_details,name="nhomem"),
    
    path('deleterestmem/<int:restid>',views.delete_rest_mem,name='rest_mem_delete'),
    path('deletephmem/<int:phid>',views.delete_ph_mem,name='ph_mem_delete'),
    path('deletehomem/<int:hoid>',views.delete_ho_mem,name='ho_mem_delete'),
    
    path('acceptrestmem/<int:restid>',views.accept_rest_mem,name='rest_mem_accept'),
    path('homemaccept/<int:hoid>',views.ho_mem_accept,name="ho_mem_accept"),
    path('phmemaccept/<int:phid>',views.ph_mem_accept,name="ph_mem_accept"),
    path('drmemaccept/<int:drid>',views.dr_mem_accept,name="dr_mem_accept"),

    path('rejecting/<int:rrid>',views.rest_mem_reject,name="rest_mem_reject"),
    path('phmemreject/<int:phid>',views.ph_mem_reject,name="ph_mem_reject"),
    path('homemreject/<int:hoid>',views.ho_mem_reject,name="ho_mem_reject"),
    path('drmemreject/<int:drid>',views.dr_mem_reject,name="dr_mem_reject"),

    path('resdashboard/',views.res_dashboard, name ="resdashboard"),
    path('phdashboard/',views.ph_dashboard,name="phdashboard"),
    
    
    path('accept',views.accept,name="accepted"),
    path('reject',views.reject,name="rejected"),
    path('waiting/',views.waiting,name="waiting"),
    
    path('waitinglist/',views.waiting_list,name="waitinglist")

]