from django.db import models

from core.models import User
from restaurant.models import Restaurant, MenuItem



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    votes = models.ManyToManyField(MenuItem, through='Vote', related_name='voted_by')
    job_title = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'menu_item', 'date')

    def __str__(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name} - {self.menu_item.name}'
