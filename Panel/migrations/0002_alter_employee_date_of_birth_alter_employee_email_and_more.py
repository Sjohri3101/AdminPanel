# Generated by Django 5.0.6 on 2024-10-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Transgender'), ('4', 'Others')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
