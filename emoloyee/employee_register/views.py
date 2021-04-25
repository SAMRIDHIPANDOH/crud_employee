from django.shortcuts import render,redirect
from .forms import Employeeforms
from .models import Employee
# Create your views here.
def emp_list(request):
    context = {'emp_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)


def emp_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = Employeeforms()
        else:
            employee = Employee.objects.get(pk=id)
            form=Employeeforms(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = Employeeforms(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Employeeforms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect("/employee/list")



def emp_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/list")





