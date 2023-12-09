from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Level(models.Model):
    level = models.CharField(max_length=30)

    def __str__(self):
        return self.level


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField()
    level_task = models.ForeignKey(Level, related_name='level_task', on_delete=models.CASCADE)
    status_task = models.ForeignKey(Status, related_name='status_task', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("detail", args=(self.slug, ))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)