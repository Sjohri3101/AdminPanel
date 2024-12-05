from django import forms
from attendance.models import *

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'check_in_time', 'check_out_time', 'status']

class AttendanceModificationForm(forms.ModelForm):
    class Meta:
        model = AttendanceModificationRequest
        fields = ['check_in_time', 'check_out_time', 'date', 'attendance_type']  # Include attendance_type
        
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_in_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'check_out_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'attendance_type': forms.Select(attrs={'class': 'form-select'}),  # Add select widget for attendance_type
        }

    # Optionally, you can add a custom validation method if needed
    def clean(self):
        cleaned_data = super().clean()
        check_in_time = cleaned_data.get("check_in_time")
        check_out_time = cleaned_data.get("check_out_time")

        if check_in_time and check_out_time and check_in_time >= check_out_time:
            raise forms.ValidationError("Check-out time must be after check-in time.")

        return cleaned_data
        

    
class ApplyLeaveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplyLeaveForm, self).__init__(*args, **kwargs)

        # Set widget attributes for styling
        self.fields['from_date'].widget.attrs = {
            "class": "form-control datepicker",
            "placeholder": "Select Date"
        }
        self.fields['to_date'].widget.attrs = {
            "class": "form-control datepicker",
            "placeholder": "Select Date"
        }
        self.fields['leave_type'].widget.attrs = {
            "class": "form-control", 
            "placeholder": self.instance.leave_type or "-- Select --"
        }
        
    class Meta:
        model = AppliedLeaveData
        fields = ['from_date', 'to_date', 'leave_type']
        
    