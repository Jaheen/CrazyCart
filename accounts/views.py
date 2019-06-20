from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as UserLogin, logout as UserLogout, authenticate
from django.contrib import messages

from .models import *
from .verification import sendVerificationEmail

#SUGGESTED TO USE CLASS BASED VIEWS FOR A LARGE PROJECT
#I USED FUNCTION BASED VIEWS FOR THIS SIMPLE PROJECT
def login(request):
    if (request.method == "GET"):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return render(request, "accounts/login.html")
    if (request.method == "POST"):
        email = request.POST.get("email")
        password = request.POST.get("password")
        authenticatedUser = authenticate(request, email=email, password=password)  #authenticate using custom user model
        if authenticatedUser is not None:
            UserLogin(request, authenticatedUser)
            user = User.objects.get(email = request.user.email)
            if (user.verified):
                return redirect("/")
            else:
                return redirect("/accounts/verifyEmail")
        else:
            messages.error(request,"Username And Password doesn't match")
            return redirect("/accounts/login")


@login_required(login_url="/accounts/login")
def verifyEmail(request):
    user = User.objects.get(email = request.user.email)
    if(request.method == "GET"):
        if not user.verified:
            sendVerificationEmail(request)
            return render(request, "accounts/verifyEmail.html")
        else:
            return redirect("/")
    elif(request.method == "POST"):
        otpStorage = OTP.objects.get(user=user) 
        sentOtp =  otpStorage.otp
        if(sentOtp == int(request.POST.get("otp"))):            
            user.verified = True
            user.save()
            messages.info(request,"Account Verified")
            return redirect("/")
        else:
            messages.error(request, "Account Verification Failed, OTP is resent please verify the new OTP")
            return redirect("/accounts/verifyEmail")


def signUp(request):
    if (request.method == "GET"):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return render(request, "accounts/signUp.html")
    if (request.method == "POST"):
        if not User.objects.filter(email=request.POST.get("email")).exists():
            if(request.POST.get("firstName")):
                firstName = request.POST.get("firstName")
            if(request.POST.get("lastName")):
                lastName = request.POST.get("lastName")
            if(request.POST.get("email")):
                email = request.POST.get("email")
            if(request.POST.get("password")):
                password = request.POST.get("password")
                createdUser = User.objects.createConsumerUser(email, firstName, lastName, password)
                user = UserLogin(request, createdUser)
                return redirect("/accounts/verifyEmail")
        else:
            messages.error(request, "Email is already registered")
            return redirect("/accounts/signUp")


def forgotPassword(request):
    return render(request, "accounts/forgotPassword.html")


@login_required(login_url="/accounts/login")
def profile(request):
    user = User.objects.get(email=request.user.email)
    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)


@login_required(login_url="/accounts/login")
def updateProfile(request):
    if (request.method == "GET"):
        user = User.objects.get(email=request.user.email)
        context = {
            "user": user,
        }
        return render(request, "accounts/updateProfile.html", context)
    if (request.method == "POST"):
        # save to model if only the parameters are available else errors will pop out
        user = User.objects.get(email=request.user.email)
        if (request.POST.get("firstName")):
            user.firstName = request.POST.get("firstName")
        if (request.POST.get("lastName")):
            user.lastName = request.POST.get("lastName")
        if (request.POST.get("mobileNumber")):
            user.mobileNumber = request.POST.get("mobileNumber")
        if (request.POST.get("permanentAddress")):
            user.permanentAddress = request.POST.get("permanentAddress")
        if (request.POST.get("city")):
            user.city = request.POST.get("city")
        if (request.POST.get("zip/pincode")):
            user.code = request.POST.get("zip/pincode")
        if (request.POST.get("country")):
            user.country = request.POST.get("country")
        if (request.POST.get("profilePicture")):
            user.profilePicture = request.FILES["profilePicture"]
        user.save()
        return redirect("/accounts/profile")


def logout(request):
    UserLogout(request)
    return redirect("/")
