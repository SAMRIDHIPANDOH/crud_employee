from django import forms
from .models import Employee

class Employeeforms(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        labels={
            'fullname': "Full Name",
            "mobile" : "Contact Number",
            "emp_code": "Employee Code"
        }
    def __init__(self,*args,**kwargs):
        super(Employeeforms,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required = False