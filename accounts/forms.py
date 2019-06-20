from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


#user creation form used by django admin if user is to be created from the django admin.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["firstName", "lastName", "email"]
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#user change form for altering the data later after creating the user.
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName', 'profilePicture', 'mobileNumber', 'permanentAddress', 'city', 'code', 'country', 'dateJoined', 'verified', 'active', 'consumerUser', 'merchantUser', 'staff', 'admin')
    def clean_password(self):
        return self.initial["password"]
