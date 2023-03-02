from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Pub', 'Published'),
        ('Drf', 'Draft'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    