from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def registrationview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboardview')
    else:
        initial_data = {'username':'','password1':'', 'password2':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/register.html', {'form':form})



def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboardview')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form':form})

def dashboardview(request):
    return render(request,'layouts/dashboard.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def viewallemployees(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request, 'CRUD/viewallemp.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Role
from datetime import datetime

def addemp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])

        print(first_name,dept_id,role_id)
        
        try:
            dept = Department.objects.get(pk=dept_id)
            role = Role.objects.get(pk=role_id)
            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept=dept,
                role=role,
                hire_date=datetime.now()
            )
            new_emp.save()
            return HttpResponse('Employee added successfully')
        except Department.DoesNotExist:
            return HttpResponse('Department does not exist')
        except Role.DoesNotExist:
            return HttpResponse('Role does not exist')
    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'departments': departments,
            'roles': roles
        }
        return render(request, 'CRUD/addemp.html', context)
    else:
        return HttpResponse('An Exception occurred! Employee has not been added')

def filteremployee(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps' : emps
        }
        return render(request, 'CRUD/viewallemp.html', context)

    elif request.method == 'GET':
        return render(request, 'CRUD/filteremp.html')
    
    else:
        return HttpResponse("No Such Data Available!")


def deleteemployee(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()  # Add parentheses to call the delete method
            return HttpResponse("Employee Removed Successfully")
        except Employee.DoesNotExist:
            return HttpResponse("Please Enter A Valid EMP ID")
    else:
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'CRUD/deleteemp.html', context)


