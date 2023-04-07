from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    user = models.ForeignKey(User, related_name='userProjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Priority(models.Model):
    priorityValue = models.IntegerField(default=1)

    def __str__(self):
        return self.priorityValue
    

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    project = models.ForeignKey(Project, related_name='projectTasks', on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, related_name='priorityTasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
