from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Priority(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = "Priorities"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=300)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
