from django.urls import path
from.import views
app_name='gmadmin'


urlpatterns=[
    path('login',views.adhome , name='login'),
    path('applications/', views.application , name='application')
    
]