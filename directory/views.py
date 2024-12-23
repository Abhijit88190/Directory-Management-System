from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def index(request):
    userdetail = UserDetails.objects.filter(status='public')

    try:
        if request.method == "POST":
            sd = request.POST['searchdata']
            userDtls = UserDetails.objects.filter(
                Q(FirstName__icontains=sd) | Q(FirstName__icontains=sd) | Q(Contact__icontains=sd), status='public')
            return render(request, 'searchData.html', locals())
    except:
        pass
    return render(request, 'index.html', locals())

def viewSearchData(request,pid):
    userdetail = UserDetails.objects.get(id=pid)
    return render(request, 'viewSearchData.html', locals())


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'login.html', locals())


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalRecord = UserDetails.objects.all().count()
    totalprivateRecord = UserDetails.objects.filter(status='private').count()
    totalpublicRecord = UserDetails.objects.filter(status='public').count()

    return render(request, 'dashboard.html', locals())


def add_Directory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Email = request.POST['Email']
        Contact = request.POST['Contact']
        Gender = request.POST['Gender']
        # Hobbies = request.POST['Hobbies']
        Hobbies = ",".join(request.POST.getlist('Hobbies'))
        placeofBirth = request.POST['placeofBirth']
        # placeofWork = request.POST['placeofWork']
        placeofWork = ",".join(request.POST.getlist('placeofWork'))
        profession = request.POST['profession']
        Address = request.POST['Address']
        print(Hobbies)
        print(placeofWork)
        try:
            userdetail = UserDetails.objects.create(FirstName=FirstName, LastName=LastName, Email=Email,
                                                    Contact=Contact,
                                                    Gender=Gender, Hobbies=Hobbies, placeofBirth=placeofBirth,
                                                    placeofWork=placeofWork, profession=profession, Address=Address,
                                                    status="public")
            error = "no"
            try:
                image = request.FILES['image']
                userdetail.image = image
                userdetail.save()
            except:
                pass
        except:
            error = "yes"

    return render(request, 'add_Directory.html', locals())


def manage_Directory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.all()
    return render(request, 'manage_Directory.html', locals())


def edit_Directory(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.get(id=pid)

    if request.method == "POST":
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Email = request.POST['Email']
        Contact = request.POST['Contact']
        Gender = request.POST['Gender']
        #Hobbies = request.POST['Hobbies']
        Hobbies = ",".join(request.POST.getlist('Hobbies'))
        placeofBirth = request.POST['placeofBirth']
        # placeofWork = request.POST['placeofWork']
        placeofWork = ",".join(request.POST.getlist('placeofWork'))
        print(placeofWork)
        profession = request.POST['profession']
        Address = request.POST['Address']
        status = request.POST['status']

        userdetail.FirstName = FirstName
        userdetail.LastName = LastName
        userdetail.Email = Email
        userdetail.Contact = Contact
        userdetail.Gender = Gender

        if Hobbies != "":
            userdetail.Hobbies = Hobbies

        if placeofWork != "":
            userdetail.placeofWork = placeofWork

        userdetail.placeofBirth = placeofBirth
        #userdetail.placeofWork = placeofWork
        userdetail.profession = profession
        userdetail.Address = Address
        userdetail.status = status

        try:
            userdetail.save()
            error = "no"
        except:
            error = "yes"

        '''try:
            Hobbies = ",".join(request.POST.getlist('Hobbies'))
            userdetail.Hobbies = Hobbies
        except:
            pass
        
        try:
            placeofWork = ",".join(request.POST.getlist('placeofWork'))
            userdetail.placeofWork = placeofWork
        except:
            pass'''

        try:
            image = request.FILES['image']
            userdetail.image = image
            userdetail.save()
        except:
            pass
    return render(request, 'edit_Directory.html', locals())


def deleteDirectory(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.get(id=pid)
    userdetail.delete()
    return redirect('manage_Directory.html')


def search_Directory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        userdetail = UserDetails.objects.filter(
            Q(FirstName__icontains=sd) | Q(LastName__icontains=sd) | Q(Contact__icontains=sd))
    except:
        userdetail = ""
    return render(request, 'search_Directory.html', locals())


def allRecord(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.all()
    return render(request, 'allRecord.html', locals())


def privateRecord(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.filter(status='private')
    return render(request, 'privateRecord.html', locals())


def publicRecord(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.filter(status='public')
    return render(request, 'publicRecord.html', locals())


def viewallRecord(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    userdetail = UserDetails.objects.get(id=pid)
    return render(request, 'viewallRecord.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')
