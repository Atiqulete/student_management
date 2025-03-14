from django.contrib import admin
from .models import Student  # Import the model

# Register the model to make it accessible in the admin panel
admin.site.register(Student)