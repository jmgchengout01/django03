from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from employees.models import Employee


class Command(BaseCommand):
    help = 'Setup initial groups and permissions'

    def handle(self, *args, **kwargs):
        hr_group, created = Group.objects.get_or_create(name='HR')
        boss_group, created = Group.objects.get_or_create(name='Boss')
        finance_group, created = Group.objects.get_or_create(name='Finance')

        # Define custom permissions
        content_type = ContentType.objects.get_for_model(Employee)
        add_employee = Permission.objects.create(
            codename='can_add_employee', name='Can add employee', content_type=content_type)
        edit_employee = Permission.objects.create(
            codename='can_edit_employee', name='Can edit employee', content_type=content_type)
        delete_employee = Permission.objects.create(
            codename='can_delete_employee', name='Can delete employee', content_type=content_type)

        # Assign permissions to groups
        hr_group.permissions.add(add_employee, edit_employee, delete_employee)
        boss_group.permissions.add(add_employee, edit_employee)
        finance_group.permissions.add(add_employee)

        self.stdout.write(self.style.SUCCESS(
            'Groups and permissions setup successfully.'))
