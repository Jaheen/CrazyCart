# CrazyCart
___
#### Attention:
##### Default admin email :   admin@admin.com
##### Default admin password : admin  
___
#### This project uses gmail as host for sending  emails, So use a gmail account with Password in settings.py file as
```python
#mail config
MAIL_TEMPLATES = os.path.join(BASE_DIR, "Templates/Mail")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# Alter here
EMAIL_HOST_USER = "yourMail@gmail.com"
EMAIL_HOST_PASSWORD = "yourPassword"
```
