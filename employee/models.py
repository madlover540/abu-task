from django.db import models

from core.models import User
from restaurant.models import Restaurant, MenuItem, Menu


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    job_title = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class MenuVote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name} - {self.menu.name}'

    class Meta:
        unique_together = ('employee', 'menu')
