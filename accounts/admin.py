from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from .models import *
from .forms import *


#This is the User Admin which links the user creation form and user change form to the django admin
#The fields may be changed as required
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'firstName', 'lastName', 'profilePicture', 'mobileNumber', 'permanentAddress', 'city', 'country', 'dateJoined', 'verified', 'active', 'consumerUser', 'merchantUser', 'staff', 'admin')
    list_filter = ('admin', 'consumerUser', 'merchantUser', 'staff', 'verified')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('firstName', 'lastName', 'profilePicture', 'mobileNumber')}),
        ('Identity',{'fields':('permanentAddress', 'city', 'code', 'country',)}),
        ('Permissions', {'fields': ('consumerUser', 'merchantUser', 'staff', 'admin', 'verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstName', 'lastName', 'profilePicture', 'mobileNumber', 'permanentAddress', 'city', 'code', 'country', 'dateJoined', 'verified', 'active', 'consumerUser', 'merchantUser', 'staff', 'admin')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(OTP)
