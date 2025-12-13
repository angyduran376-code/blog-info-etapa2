from .settings import * 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'g4informatorio@gmail.com'
EMAIL_HOST_PASSWORD = 'Informatorio+5202'
    
DATABASES ={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD':'8606',
        'HOST':'localhost',
        'PORT':'3306',
    }   
}