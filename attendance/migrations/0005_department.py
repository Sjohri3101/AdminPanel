# Generated by Django 5.0.6 on 2024-10-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_holidays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_head', models.CharField(max_length=100)),
            ],
        ),
    ]
