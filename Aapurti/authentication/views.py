from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import facebook as fb
import logging
from .models import JobDetails


logging.basicConfig(level=logging.INFO)

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

        myuser.save()

        messages.success(request, 'Your Account has been created successfully')

        return redirect('signin')

    return render(request, "authentication/signup.html")


def main(request):

    JobDetailsData = JobDetails.objects.all()

    data = {
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

        if user is not None:
            login(request, user)
            fname = user.first_name

            # return render(request, "authentication/main.html", {"fname":fname}, JobDetailsData)
            return redirect('/main')
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


def fbPost(request):

    if request.method == "POST":

        api_req = request.POST['Approval']
        api_project = request.POST['social']
        api_description = request.POST['Description']
        #return HttpResponse(api_description)
        if api_req == "on" and api_project == "Facebook":
            access_token = "EAAM6XmDmYZCgBAM272OOF12zzdLqfZAWt20vwRtzV04Mckci5DgxiR1xaLy4JW2fePzaUZCtpWqTKLNZAKi8TQCfpugcgwXASmrhIZC3ZAdhBqtl8lDcCogptDJsaK3EiHZCZBZBBYH1gZCjD6ioZCWkQqAkEDI0nIC6FC7MzLgaIwmChmag0JpDzcdtgIZCruNWyfMZD"
            myobject = fb.GraphAPI(access_token)
            messages.success(request, 'Post Successful !!!')
            myobject.put_object("me", "feed", message= api_description)
            return redirect('main')
            #return render(request, "authentication/fb-post1.html")

        else:
            messages.error(request, 'Select valid Posting page')
            return redirect('main')

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

            return render(request, "authentication/vendor.html", {"fname":fname})
            #return redirect('/main')
            # return main(request, {"fname":fname})

        else:
            messages.error(request, 'Invalid UserName or Password')
            # messages = 'Invalid UserName or Password'
            # return messages
            return redirect('/vendorsignin')
    else:
        return render(request, "authentication/vendorsignin.html")



def vendor(request):
    return render(request, "authentication/vendor.html")