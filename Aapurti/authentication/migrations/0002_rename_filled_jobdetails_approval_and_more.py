# Generated by Django 4.1.5 on 2023-01-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetails',
            old_name='filled',
            new_name='Approval',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='last_date',
        ),
    ]