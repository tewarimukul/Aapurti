from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

POST_TYPE = (
    ('1', "Facebook"),
    ('2', "Twitter"),
)

class JobDetails(models.Model):
    jobid = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    primary_skill = models.CharField(max_length=100)
    level=models.IntegerField()
    project=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=POST_TYPE, max_length=10)
    Approval = models.BooleanField(default=False)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isVendor = models.BooleanField(default=False)
    birthday = models.DateField()
    Gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'),('FEMALE', 'FEMALE')]
    )
    phone = models.CharField(max_length=10)

def __str__(self):
    return self.user.username

class candidatedetails(models.Model):
    jobid = models.IntegerField()
    user = models.CharField(default="User", max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    candidatename = models.CharField(max_length=100)
    pancard = models.CharField(max_length=20)
    phone = models.IntegerField()
    
    
    
    