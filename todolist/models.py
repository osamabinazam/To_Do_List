from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# Model that hold task in database
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)    # Setting relation with user through foreign key. If user deleted all his tasks will be deleted
    title = models.CharField(max_length=200 , null=True)                # Hold the title of the task
    description = models.TextField(null=True)                           # Hold the description of the task
    complete = models.BooleanField(default=False)                       # Check particular item or task is completed or not 
    created = models.DateTimeField(auto_now_add=True);                  # Time when new Task is created

    def __str__(self) :
        return self.title
    class Meta:
        ordering = ['complete']
     