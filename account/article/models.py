from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} | {self.author}"