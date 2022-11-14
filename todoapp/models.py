from django.db import models

# Create your models here.
class todotask(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=200)
    task_desc = models.TextField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_title