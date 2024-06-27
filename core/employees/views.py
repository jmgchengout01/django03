from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeCreationForm, EmployeeUpdateForm, GroupForm, UserGroupForm, PermissionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .decorators import multiple_permissions_required
from django.contrib.auth.models import Group, Permission, User


# @method_decorator(permission_required('employees.can_add_employee'), name='dispatch')
@method_decorator(multiple_permissions_required(['employees.can_add_employee', 'employees.can_edit_employee', 'employees.can_delete_employee']), name='dispatch')
class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeCreationForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee-list')


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'


@method_decorator(permission_required('employees.change_employee'), name='dispatch')
class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:employee-list')


@method_decorator(permission_required('employees.delete_employee'), name='dispatch')
class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employees:employee-list')


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'employees/group_list.html'


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'employees/group_form.html'
    success_url = reverse_lazy('employees:group-list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'employees/group_form.html'
    success_url = reverse_lazy('employees:group-list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'employees/group_confirm_delete.html'
    success_url = reverse_lazy('employees:group-list')


class UserGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserGroupForm
    template_name = 'employees/user_group_form.html'
    success_url = reverse_lazy('user-list')


@method_decorator(multiple_permissions_required(['auth.add_permission', 'auth.change_permission', 'auth.delete_permission']), name='dispatch')
class PermissionListView(LoginRequiredMixin, ListView):
    model = Permission
    template_name = 'employees/permission_list.html'
    success_url = reverse_lazy('employees:permission-list')


@method_decorator(multiple_permissions_required(['auth.add_permission']), name='dispatch')
class PermissionCreateView(LoginRequiredMixin, CreateView):
    model = Permission
    form_class = PermissionForm
    template_name = 'employees/permission_form.html'
    success_url = reverse_lazy('employees:permission-list')


@method_decorator(multiple_permissions_required(['auth.change_permission']), name='dispatch')
class PermissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Permission
    form_class = PermissionForm
    template_name = 'employees/permission_form.html'
    success_url = reverse_lazy('employees:permission-list')


@method_decorator(multiple_permissions_required(['auth.delete_permission']), name='dispatch')
class PermissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Permission
    template_name = 'employees/permission_confirm_delete.html'
    success_url = reverse_lazy('employees:permission-list')
