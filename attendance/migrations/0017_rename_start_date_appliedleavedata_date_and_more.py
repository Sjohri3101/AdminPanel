# Generated by Django 5.0.6 on 2024-10-25 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_appliedleavedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliedleavedata',
            old_name='start_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='appliedleavedata',
            name='end_date',
        ),
    ]
