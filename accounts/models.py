from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from .userManager import UserManager


# Custom user must override the builtin methods and manager.
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address', primary_key=True, max_length=255, unique=True)
    firstName = models.CharField(verbose_name="First Name", max_length=100)
    lastName = models.CharField(verbose_name="Last Name", max_length=100)
    profilePicture = models.ImageField(verbose_name="Profile Picture", upload_to="Accounts/Users/ProfilePictures", default="Accounts/Users/ProfilePictures/defaultAvatar.png")
    mobileNumber = models.CharField(verbose_name="Mobile number", max_length=20, null=True)
    permanentAddress = models.TextField(verbose_name="Permanent Address", null=True)
    city = models.CharField(verbose_name="City", max_length=30, null=True)
    code = models.CharField(verbose_name="Zip/Pin Code", max_length=15, null=True)
    country = models.CharField(verbose_name="Country", max_length=30, null=True)
    dateJoined = models.DateTimeField(verbose_name="Date Joined", default=timezone.now)
    verified = models.BooleanField(verbose_name="Verified ", default=False)
    active = models.BooleanField(default=True)
    consumerUser = models.BooleanField(default=False)
    merchantUser = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # notice the absence of a "Password field", that's built in.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
        
# OTP model used to store the sent OTP for verification
class OTP(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    otp = models.IntegerField(verbose_name="OTP Generated", default=000000)
    dateTime = models.DateTimeField(verbose_name="Date And Time Generated", default=timezone.now)
    def __str__(self):
        return self.user.email
    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"
