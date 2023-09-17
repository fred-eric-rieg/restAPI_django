import django
from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.name}'
    

class Priority(models.Model):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'

    PRIORITIES = {
        Low, 'Low',
        Medium, 'Medium',
        High, 'High',
    }

    name = models.CharField(max_length=6,
                            choices=PRIORITIES,
                            default=Low)

    def __str__(self):
        return f'({self.id}) {self.name}'


class Subtask(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.name}'


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE, default='Low')
    due_date = models.DateTimeField(default=django.utils.timezone.now)
    assigned_to = models.ManyToManyField('Contact', symmetrical=False, related_name='assigned_to')
    subtask = models.ForeignKey('Subtask', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.title}'