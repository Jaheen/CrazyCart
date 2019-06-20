from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from pyotp import TOTP
from base64 import b32encode
from django.conf import settings

from .models import *

# Pyotp module is used in this project
# STEPS USED HERE
# FOLLOW THE NUMBERS
def generatePin(data):
    # 3) INORDER TO GENERATE OTP FROM PYOTP MODULE WE NEED A BASE32 KEY
    encodedData = b32encode(data.encode("utf-8"))
    # 4) LET'S CONVERT THE EMAIL ID TO BASE32 SINCE EMAIL ID IS UNIQUE
    # 5) PASS THE CONVERTED STRING TO TOTP() TO GENERATE OTP
    otp = TOTP(encodedData.decode("utf-8")).now()
    # 6) GENERATE OTP
    return otp

def sendVerificationEmail(request):
    # 1) GET THE USER'S EMAIL USING REQUEST PROVIDED FROM THE REQUEST
    email = request.user.email
    # 2) GENERATE OTP USING THE EMAIL ADDRESS
    otp = generatePin(email)
    # 7) GET OTHER DETAILS FOR SENDING EMAIL
    toAddress = email
    fromAddress = settings.EMAIL_HOST_USER

    # 8) GET THE USER OBJECT FOR CREATING A ROW WITH SAME NAME IN OTP TABLE
    user = User.objects.get(email=email)
    
    # 9) OTP ROW FOR THE USER NOT EXISTS (ie. NEW SIGNUP)
    if not OTP.objects.filter(user=user).exists():
        # 10) CREATE A ROW FOR THE USER WITH NAME AS USER'S EMAIL ID
        otpStorage = OTP.objects.create(user=user)
        otpStorage.otp = otp
        otpStorage.dateTime = timezone.now()
        # 11) SAVE OTP TO THE ROW NAMED WITH USER'S EMAIL
        otpStorage.save()
    else:
        # 12) IF EXISTS (ie. USER ALREADY CREATED BUT NOT VERIFIED OR VERIFICATION FAILED)
        otpStorage = OTP.objects.get(user=user)
        otpStorage.otp = otp
        otpStorage.dateTime = timezone.now()
        # 13) SAVE THE OTP AS IN STEP 11
        otpStorage.save()

    # 14) OTHER DETAILS LIKE SUBJECT .etc
    subject = "CrazyCart Email Verification"
    # 15) OPEN THE EMAIL TEMPLATE (text to be sent or HTML email template) which constitute the body of the letter.
    template = open(settings.MAIL_TEMPLATES + "/welcome.txt","r")
    # 16) REPLACE USER WITH USER'S NAME FROM THE USER OBJECT
    message = template.read().replace("user", user.firstName)
    message = message+"Your OTP is :" + otp + ". Enter this OTP to get your account verified."
    #  17) SEND THE EMAIL
    send_mail(subject, message, fromAddress, (toAddress,))
