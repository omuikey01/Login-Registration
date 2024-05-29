from django.shortcuts import render
from .models import Student

# Create your views here.

def indexfun(request) :
    return render(request, "index.html")

def regisfun(request):
    return render(request, "regis.html")

def loginfun(request):
    return render(request, "login.html")

# if request.method == "POST" :

def registration(request):
    if request.method == "POST":
        namevar = request.POST['name']
        coursevar = request.POST['course']
        feesvar = request.POST['fees']
        passvar = request.POST['pass']
        confirmpassvar = request.POST['cpass']
        emailvar = request.POST['email']

        if passvar != confirmpassvar :
            return render (request, "regis.html", {"errmsg" : "Password and Confirma Password not Match"})
        else :
            Student.objects.create(name = namevar,
                                   email = emailvar,
                                   course = coursevar,
                                   fees = feesvar,
                                   password = passvar,
                                   confirm_password = confirmpassvar
                                   )
            return render (request, "login.html")
        
    else:
        print("Method Get ")


def login(request):
    if request.method == "POST":
        emailvar = request.POST['email']
        passvar = request.POST['pass']

        database_data = Student.objects.all()
        for data in database_data :
            # print(data)
            # print(data.email) name, password
            if  data.email == emailvar and data.password == passvar : 
                return render(request, "dash.html", {"username":data.name})
