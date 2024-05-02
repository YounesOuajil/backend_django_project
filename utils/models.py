from django.db import models
from datetime import date
    # access_token = models.JSONField()



class Intern(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)
    education = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name 

class Internship(models.Model):
    recruiter = models.ForeignKey('authentication.Recruiter', on_delete=models.CASCADE, related_name='internships') 
    interns = models.ManyToManyField(Intern, related_name='internships',null=True)  
    subject = models.CharField(max_length=100) 
    email = models.EmailField()  
    location = models.CharField(max_length=100) 
    deadline = models.DateField(default=date.today)  
    
    def __str__(self):
        return self.subject
    
