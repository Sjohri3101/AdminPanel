from django.contrib import admin

from alert.models import Alert

# Register your models here.
class AlertAdmin(admin.ModelAdmin):
    list_display = ['id', 'alert_type', 'alert_image','heading', 'sub_heading', 'summary', 'created_at']
    
    
admin.site.register(Alert, AlertAdmin)