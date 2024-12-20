# Generated by Django 5.0.6 on 2024-10-30 09:45

import utilities.validators.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alert', '0002_delete_alert'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('warning', 'warning'), ('error', 'error'), ('success', 'success'), ('information', 'information'), ('job', 'job'), ('alert', 'alert')], max_length=100)),
                ('alert_image', models.ImageField(blank=True, default='img/dummy-profile-pic.png', null=True, upload_to='alerts', validators=[utilities.validators.validators.image_file_validator])),
                ('heading', models.TextField(max_length=200)),
                ('sub_heading', models.TextField(blank=True, max_length=200, null=True)),
                ('summary', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ManyToManyField(limit_choices_to={'is_active': 1}, related_name='employee_alert', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
