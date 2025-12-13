from .settings import *
    
DATABASES ={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }   
}