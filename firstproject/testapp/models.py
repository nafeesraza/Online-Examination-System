from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    esal=models.FloatField()
    def __str__(self):
        return self.ename+' '+str(self.esal)