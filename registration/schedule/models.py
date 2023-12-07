from django.db import models

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grade_point_avg = models.DecimalField(max_digits=3, decimal_places=2)
    major = models.CharField(max_length=50)
    year_in_school = models.CharField(max_length=30, choices=YEAR_IN_SCHOOL_CHOICES)
