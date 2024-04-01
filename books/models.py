from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title