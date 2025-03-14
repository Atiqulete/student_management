from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('ETE', 'Electronics & Telecommunication Engineering'),
        ('CSE', 'Computer Science & Engineering'),
        ('EEE', 'Electrical & Electronic Engineering'),
        ('BBA', 'Business Administration'),
        ('ENG', 'English Literature'),
        ('LLB', 'Law'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('ARCH', 'Architecture'),
        ('BIO', 'Biotechnology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
        ('MATH', 'Mathematics'),
        ('STAT', 'Statistics'),
        ('MED', 'Medicine'),
        ('PHAR', 'Pharmacy'),
        ('NUR', 'Nursing'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('HRM', 'Human Resource Management'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default='ETE')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_course_display()}"
