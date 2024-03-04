# models.py
from django.db import models

class LevelOfEducation(models.Model):
    level = models.CharField(max_length=50, verbose_name="Level of Education")

    def __str__(self):
        return self.level


class StudentInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")
    level_of_education = models.ForeignKey(LevelOfEducation, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Level of Education")

    def __str__(self):
        return str(self.id)
