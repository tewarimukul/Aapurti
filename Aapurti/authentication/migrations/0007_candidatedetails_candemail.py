# Generated by Django 4.1.5 on 2023-01-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_candidatedetails_jobid'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatedetails',
            name='candEmail',
            field=models.CharField(default='', max_length=30),
        ),
    ]