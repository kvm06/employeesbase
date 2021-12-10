from django.forms import ModelForm
from .models import Employee, Department, Programminglanguage

class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'age', 'gender', 'department', 'prog_language']

    def __init__(self, *args, **kwargs):
        super(AddEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'id': 'name_id'})

class AddDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'floor']

class AddProgLanguageForm(ModelForm):
    class Meta:
        model = Programminglanguage
        fields = ['language']