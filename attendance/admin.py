from django.contrib import admin
from attendance.models import *

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    class Media:
        js = ('static/js/attendance.js',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form
    list_display = ['id', 'employee', 'date', 'check_in_time', 'check_out_time', 'total_duration', 'status']
    
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'holiday', 'year']
    

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name', 'department_head']
    
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'department', 'leave_type', 'total_leaves', 'remaining_leaves', 'used_leaves']
    
class AppliedLeavesAdmin(admin.ModelAdmin):
    list_display = ['id', 'request_id', 'employee', 'leave_type','leave_apply_date','from_date', 'to_date', 'no_of_days', 'status']

class AttendanceModificationRequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'request_employee', 'check_in_time', 'check_out_time', 'date', 'modified_at', 'status', 'attendance_type']
    
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Holidays, HolidaysAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(EmployeeLeave, LeaveAdmin)
admin.site.register(AppliedLeaveData, AppliedLeavesAdmin)
admin.site.register(AttendanceModificationRequest, AttendanceModificationRequestAdmin)



