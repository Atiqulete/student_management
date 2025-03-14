from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('EEE', 'Electrical & Electronic Engineering'),
        ('BBA', 'Business Administration'),
        ('ENG', 'English Literature'),
        ('LLB', 'Law'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default='CSE')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_course_display()}"
