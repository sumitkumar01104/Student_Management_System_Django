from django.db import models
from datetime import date

class Form(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    DoB = models.DateField(default=date(2000, 1, 1))
    mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name
