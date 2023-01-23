from django.db import models
from django.db import models
from django.utils import timezone

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

    