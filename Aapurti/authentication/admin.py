from django.contrib import admin
from .models import JobDetails


@admin.register(JobDetails)
class DataAdmin(admin.ModelAdmin):
    pass
    #list_display=('jobid','primary_skill', 'project','description')

# Register your models here.
