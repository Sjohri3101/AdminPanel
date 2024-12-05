from django.contrib import admin
from Panel.models import Employee , EmployeeProfile, EmployeeQualification, EmployeeSkills
# Register your models here.

class EmployeeSkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'skill', 'level']
    
class EmployeeQualificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'degree', 'percentage', 'division']
    
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee']

    
admin.site.register(Employee)
admin.site.register(EmployeeSkills, EmployeeSkillsAdmin)
admin.site.register(EmployeeQualification, EmployeeQualificationAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
