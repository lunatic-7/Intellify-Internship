from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact, Profile

# Create your views here.
def home(request):
    # Request Current User
    current_user = request.user
    # If No User Available, means AnonymousUser, Then don't run the following code
    if str(current_user) != "AnonymousUser":
        # Getting profile of corresponding user
        profile = Profile.objects.get(user=current_user)
        # Passing profile as context to home
        context = {'profile': profile}
        return render(request, "school/home.html", context)
    return render(request, "school/home.html")

def contact(request):
    # Getting user contact details using Post request
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        # Saving the details to DB
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        # Displaying a Success message using Django message module.
        messages.success(request, "Request Sent Successfully!")
    return render(request, 'school/contact.html')

def sregister(request):
    # Getting Student registration details using Post request 
    if request.method == "POST":
        # Get the post parameters
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        studclass = request.POST["studclass"]
        section = request.POST["section"]
        stream = request.POST["stream"]
        rollno = request.POST["rollno"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check if password and repeat password match
        if pass1 != pass2:
            # Displaying a Error message using Django message module.
            messages.error(request, 'Passwords did not match!')
            # Redirecting to home page
            return redirect("home")

        # Create the user
        myuser = User.objects.create_user(fname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        # Saving corresponding student's profile details
        profile = Profile(user=myuser, studclass=studclass, section=section, stream=stream, rollno=rollno)
        profile.save()

        # Displaying a Success message using Django message module.
        messages.success(request, "Account created, Now you can log in to your account!")
        return redirect("home")
    return render(request, "school/sregister.html")

def tregister(request):
    # Getting Student registration details using Post request 
    if request.method == "POST":
        # Get the post parameters
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        classtaught = request.POST["classt"]
        phone = request.POST["phone"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check if password and repeat password match
        if pass1 != pass2:
            messages.error(request, 'Passwords did not match!')
            # Redirecting to home page
            return redirect("home")

        # Create the user
        myuser = User.objects.create_user(fname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        # Saving corresponding teacher's profile details
        profile = Profile(user=myuser, subject=subject, classtaught=classtaught, phone=phone)
        profile.save()

        # Displaying a Success message using Django message module.
        messages.success(request, "Account created, Now you can log in to your account!")
        return redirect("home")
    return render(request, "school/tregister.html")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        # Authenticating User
        user = authenticate(username=loginusername, password=loginpassword)
        # If User Credentials are available in DB then log him/her in
        if user is not None:
            login(request, user)
            # Displaying a Success message using Django message module.
            messages.success(request, "Successfully logged in!")   
            # Redirect to home page
            return redirect("home")
        # If user is not available
        else:
            # Displaying a Error message using Django message module.
            messages.error(request, "Invalid Credentials!")
            # Redirect to home page
            return redirect("home")
    return render(request, "school/login.html")

def handleLogout(request):
    # Handling log out
    logout(request)
    # Displaying a Success message using Django message module.
    messages.success(request, "Successfully logged out!")
    # Redirect to home page
    return redirect("home")

def student(request):
    # Getting Cureent logged in user deatials and it to student's profile page
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    context = {'profile': profile}
    return render(request, "school/student.html", context)

def teacher(request):
    # Getting Cureent logged in user deatials and it to student's profile page
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    context = {'profile': profile}
    return render(request, "school/teacher.html", context)