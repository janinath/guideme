# Generated by Django 4.1.3 on 2023-07-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_registrationcustomer_email_registrationcustomer_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmember',
            name='type',
            field=models.TextField(db_column='user type', null=True),
        ),
    ]
