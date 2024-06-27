from django.core.management.base import BaseCommand
from django.db import transaction
# from departments.models import Department
from categories.models import Category
from tags.models import Tag
# from privileges.models import Privilege


class Command(BaseCommand):
    help = 'Reset and repopulate data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        # Department.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()
        # Privilege.objects.all().delete()
        self.stdout.write('Populating data...')
        self.populate_data()
        self.stdout.write(self.style.SUCCESS(
            'Data reset and repopulated successfully.'))

    @transaction.atomic
    def populate_data(self):
        # Department.objects.create(name='HR')
        # Department.objects.create(name='IT')
        # Department.objects.create(name='Sales')
        Category.objects.create(name='Full-time')
        Category.objects.create(name='Part-time')
        Category.objects.create(name='Intern')
        Tag.objects.create(name='Experienced')
        Tag.objects.create(name='Newbie')
        # Privilege.objects.create(name='Add Employee')
        # Privilege.objects.create(name='Edit Employee')
        # Privilege.objects.create(name='Delete Employee')
