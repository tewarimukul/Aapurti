from django.contrib import admin
from authentication.models import Vendor
from .models import JobDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import candidatedetails

@admin.register(JobDetails)
class DataAdmin(admin.ModelAdmin):
    pass
    #list_display=('jobid','primary_skill', 'project','description')
# Register your models here.

class VendorInline(admin.StackedInline):
    model = Vendor
    can_delete = False
    verbose_name_plural = 'Vendor'

class CustomizedUserAdmin (UserAdmin):
    inlines = (VendorInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Vendor)

@admin.register(candidatedetails)
class DataAdmin(admin.ModelAdmin):
    pass