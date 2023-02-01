from contextlib import nullcontext
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import facebook as fb
import logging
from .models import JobDetails
from .models import Vendor
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from cryptography.fernet import Fernet
from django.contrib.auth.hashers import make_password
import base64
from .models import candidatedetails

logging.basicConfig(level=logging.INFO)

# Encrypt URL


def encrypt_name(name):
    encname = name.encode("ascii")
    encname = base64.b64encode(encname)
    encname = encname.decode("ascii")
    return encname


def decrypt_name(name):
    decname = name.encode('ascii')
    decname = base64.b64decode(decname)
    decname = decname.decode('ascii')
    return decname

# Create your views here.


def home(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        # myvendor = Vendor()
        myuser.save()

        messages.success(request, 'Your Account has been created successfully')

        return redirect('signin')

    return render(request, "authentication/signup.html")


def main(request, name):

    JobDetailsData = JobDetails.objects.all()
    fstname = decrypt_name(name.split("+")[0])
    lstname = decrypt_name(name.split("+")[1])
    usern = decrypt_name(name.split("+")[2])

    data = {
        'name': name,
        'fname': fstname.title(),
        'lname': lstname.title(),
        'username': usern,
        'JobDetailsData': JobDetailsData
    }
    # return render(request,"authentication/fb-post1.html", data)
    return render(request, "authentication/main.html", data)


def fb_post1(request):

    JobDetailsData = JobDetails.objects.all()

    data = {
        'JobDetailsData': JobDetailsData
    }
    return render(request, "authentication/fb-post1.html", data)
    # return render(request,"authentication/main.html", data)


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        fname = user.first_name
        lname = user.last_name
        usern = user.username

        fname_enc = encrypt_name(fname)
        lname_enc = encrypt_name(lname)
        usern = encrypt_name(usern)

        name = fname_enc + "+" + lname_enc + "+" + usern

        if user is not None:
            login(request, user)

            # return render(request, "authentication/main.html", {fname:fname})
            # return render(request, "authentication/main.html", {"fname":fname}, JobDetailsData)
            return redirect('/main/' + str(name), name=name)
            # return main(request, {"fname":fname})

        else:
            messages.error(request, 'Invalid UserName or Password')
            # messages = 'Invalid UserName or Password'
            # return messages
            return redirect('/signin')
    else:
        return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    return redirect('home')


def fbPost(request, name):

    disable_warnings(InsecureRequestWarning)
    if request.method == "POST":
        api_req = request.POST['Approval']
        api_project = request.POST['social']
        api_description = request.POST['Description']
        # return HttpResponse(api_description)
        if api_req == "on" and api_project == "Facebook":
            access_token = "EAAM6XmDmYZCgBAI1UZBmvrhz8b0nxwt6Xv0LhnaS3bNckn3ZAqWTZCLwwW9O3IHTKAPzYyYycc0rrXOFqytrkvD8xy8pFBIeohJIXRZBBaSjZCuENyIUNZCZA9m0j9IiaAztR4bG57mljgNMwaakFP1nbH5ybSFXmzR1tNTZCOYEdLTwGzGZC2x8A9h8RmZCOJDVC4ZD"
            myobject = fb.GraphAPI(access_token)
            myobject.put_object("me", "feed", message=api_description)
            messages.success(request, 'Post Successful !!!')
            return redirect('main', name=name)
            # return render(request, "authentication/fb-post1.html")

        else:
            messages.error(request, 'Select valid Posting page')
            return redirect('main', name=name)

    else:
        return redirect('home')
        # return HttpResponse("Kuch Nahi Hua  " + str(request.method))

        # return render(request,"authentication/index.html")


# PageId=101328056193847


def vendorsignin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            lname = user.last_name
            usern = user.username

            fname_enc = encrypt_name(fname)
            lname_enc = encrypt_name(lname)
            usern = encrypt_name(usern)

            name = fname_enc + "+" + lname_enc + "+" + usern

            return redirect('/vendor/' + str(name), name=name)
            # return render(request, "authentication/vendor.html", {"fname":fname})
            # return redirect('/main')
            # return main(request, {"fname":fname})

        else:
            messages.error(request, 'Invalid UserName or Password')
            # messages = 'Invalid UserName or Password'
            # return messages
            return redirect('/vendorsignin')
    else:
        return render(request, "authentication/vendorsignin.html")


def vendor(request, name):
    fstname = decrypt_name(name.split("+")[0])
    lstname = decrypt_name(name.split("+")[1])
    usern = decrypt_name(name.split("+")[2])

    data = {
        'name': name,
        'fname': fstname.title(),
        'lname': lstname.title(),
        'username': usern,
    }
    return render(request, "authentication/vendor.html", data)


def candidate(request):

    messages.success(request, '')
    messages.error(request, '')
    if request.method == "POST":
        jobdetails = request.POST['Job Details']
        candidatename = request.POST['Candidate Name']
        pancard = request.POST['PAN Card']
        phonenumber = request.POST['Phone Number']
        name = request.POST['enc_name']
        emailadd = request.POST['Email']
        emailDomain = request.POST['Email_domain']

        email = emailadd + "@" + emailDomain

        fstname = decrypt_name(name.split("+")[0])
        lstname = decrypt_name(name.split("+")[1])
        usern = decrypt_name(name.split("+")[2])

        data = {
            'name': name,
            'fname': fstname.title(),
            'lname': lstname.title(),
            'username': usern,
            }
        
        candidate= candidatedetails(jobid= jobdetails,candidatename= candidatename,pancard= pancard,phone= phonenumber,user=usern, candEmail=email)
        candidate.save()
        
        messages.success(request, 'Profile Save Successful !!!')
        return redirect('vendor', name=name)
        #return render(request, "authentication/vendor.html", data)
