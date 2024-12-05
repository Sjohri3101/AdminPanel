from django.db import models
from Panel.models import Employee
from utilities.validators.validators import image_file_validator

# Create your models here.
class Alert(models.Model):
    alter_types =[
        ('warning', 'warning'),
        ('error', 'error'),
        ('success', 'success'),
        ('information', 'information'),
        ('job', 'job'),
        ('alert', 'alert'),
        
    ]
    employee = models.ManyToManyField(Employee, limit_choices_to={'is_active': 1},related_name="employee_alert",blank=False)
    alert_type = models.CharField(max_length=100, null=False, blank=False, choices=alter_types)
    alert_image = models.ImageField(upload_to='alert', default='alert/alert.jpg', blank=True, null=True,validators=[image_file_validator])
    heading = models.TextField(max_length=200, null=False, blank=False)
    sub_heading = models.TextField(max_length=200, null=True, blank=True)
    summary = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.heading
    