from django import forms
from django.contrib.auth.models import User, Group, Permission
from .models import Employee, Category, Tag


class EmployeeCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')])
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea)
    country = forms.CharField(max_length=50)
    province = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    area_code = forms.CharField(max_length=10)
    # departments = forms.ModelMultipleChoiceField(
    #     queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    # privileges = forms.ModelMultipleChoiceField(
    #     queryset=Privilege.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Employee
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'date_of_birth',
            'address',
            'country',
            'province',
            'city',
            'area_code',
            'categories',
            'tags',
            # 'departments',
            # 'privileges'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        employee = super().save(commit=False)
        employee.user = user
        if commit:
            employee.save()
            self.save_m2m()
        return employee


class EmployeeUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')])
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea)
    country = forms.CharField(max_length=50)
    province = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    area_code = forms.CharField(max_length=10)
    # departments = forms.ModelMultipleChoiceField(
    #     queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    # privileges = forms.ModelMultipleChoiceField(
    #     queryset=Privilege.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Employee
        fields = [
            'middle_name',
            'gender',
            'date_of_birth',
            'address',
            'country',
            'province',
            'city',
            'area_code',
            'categories',
            'tags',
            # 'departments',
            # 'privileges'
        ]

    def save(self, commit=True):
        employee = super().save(commit=False)
        user = employee.user
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            employee.save()
            self.save_m2m()
        return employee


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']


class UserGroupForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(), required=True)
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['groups', 'user_permissions']


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name', 'codename', 'content_type']
