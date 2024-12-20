# Generated by Django 5.0.6 on 2024-10-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('Finance', 'Finance'), ('Sales', 'Sales and Marketing'), ('Operations', 'Operations'), ('Customer Service', 'Customer Service'), ('Research and Development', 'R&D'), ('Legal', 'Legal Department'), ('Admin', 'Administration'), ('Logistics', 'Logistics')], max_length=100),
        ),
    ]
