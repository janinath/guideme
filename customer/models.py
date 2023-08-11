from django.db import models


# Create your models here.
class Contactmessage (models.Model) :
    contact_email = models.TextField(max_length = 100,db_column='email')
    contact_message = models.TextField(max_length = 1000,db_column='message')
    class Meta :
        db_table='contactmessage'
        
class Registrationcustomer(models.Model) :
    fname = models.TextField(max_length=50,db_column='firstname',null=True)
    lname = models.TextField(max_length=50,db_column='lastname',null=True)
    email = models.TextField(max_length=100,db_column='mail',null=True)
    mob = models.TextField(max_length=10,db_column='mobile',null=True)
    city = models.TextField(max_length=50,db_column='city',null=True)
    state = models.TextField(max_length=50,db_column='state',null=True)
    crtepswd = models.TextField(max_length=100,db_column='createdpassword',null=True)
    pswd = models.TextField(max_length=100,db_column='password',null=True)
    otp = models.TextField(max_length=6,db_column='otp',null=True)
    status = models.TextField(max_length=10,db_column='status',null=True)
    class Meta :
        db_table='customer_registration_details'
        

