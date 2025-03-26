from django.db import models


class User(models.Model):  # Making custom user model to store user details
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12, blank=True)
    age= models.IntegerField(default=18)
   
    def __str__(self):
        return self.name
    
class Task_Detail(models.Model): # Model to store all data and details related Task 
    users = models.ManyToManyField(User, related_name='tasks') # As per requirement the one user can have multiple task and one task can have multiple users 
    task_name= models.CharField(max_length=100)
    description = models.TextField()
    task_type= models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True, blank=True)
    status= models.BooleanField(default=True)
    
    def __str__(self):
        return self.task_name