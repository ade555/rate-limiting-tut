from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now=True, auto_now_add=False)
    author_email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    