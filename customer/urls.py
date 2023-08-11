from django.urls import path
from.import views
app_name='customer'


urlpatterns=[
    path('',views.cuhome ,name="ncuhome"),
    
    path('sign',views.signin , name="nsign"),
    path('user', views.userpage,name="userpg"),
    path('userin', views.userinpage,name="userinpg"),
    path('rest', views.vrest,name="nrest"),
    path('deliciaRest', views.vdeliciaRest,name="ndeliciaRest"),
    path('verifyotp',views.otpverification,name="otpverify"),
    path('login',views.login,name='login'),
    path('customerdetail',views.customerdetails,name='customerdetails_n'),
    
    path('customerupdate',views.cust_update_v,name='customerupdate'),
    path('deletecustomer/<int:customerid>',views.delete_customer_v, name="cust_delete_n"),
    path('custupdate/<int:customerid>',views.cust_update_v, name="cust_update_n"),
    path('checkemailexist',views.checkemailuser,name='checkemail'),
    path('otp',views.cust_otp_v,name="cust_otp_n"),
    path('hotel',views.hotels,name='hotel'),
    path('plslogin',views.plslogin,name='loginpls'),
    path('photographer',views.photographer,name='photographer'),
    path('driver',views.driver,name='driver'),
    path('guide',views.guide,name='guide'),
    path('register1',views.register1,name='register1')
    
]