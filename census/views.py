from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import AddEmployeeForm, AddDepartmentForm, AddProgLanguageForm
from .models import Employee
from django.contrib import messages

# Create your views here.
def add(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        form = AddEmployeeForm()
    print(type(form))
    return render(request, 'census/add.html', {'form': form})


def list(request):
    employees = Employee.objects.all()
    return render(request, 'census/list.html', {'employees': employees})


def edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = AddEmployeeForm(instance=employee)
    return render(request, 'census/edit.html', {'form': form})


def delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('list')


def add_department(request):
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, f'Отдел "{form.instance}" успешно добавлен')
            return redirect('success')
    else:
        form = AddDepartmentForm()
    return render(request, 'census/add_department.html', {'form': form})


def add_language(request):
    if request.method == 'POST':
        form = AddProgLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, f'Язык программирования "{form.instance}" успешно добавлен')
            return redirect('success')
    else:
        form = AddProgLanguageForm()
    return render(request, 'census/add_language.html', {'form': form})


def success(request):
    return render(request, 'census/success.html')
