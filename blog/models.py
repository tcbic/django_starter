from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# What are the things we actually want to save to the database?
# Make a Post model that inherits from the Django Model class.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title