from django.db import models

class stu_m(models.Model):
    name=models.CharField(max_length=100, verbose_name="Student Name")
    age=models.PositiveIntegerField()
    address=models.TextField()

    def __str__(self):
        return f"{self.name}"
