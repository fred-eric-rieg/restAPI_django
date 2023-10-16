import django
from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.name}'
    

class Completed(models.Model):
    Todo = 'Todo'
    InProgress = 'In Progress'
    AwaitingFeedback = 'Awaiting Feedback'
    Done = 'Done'

    COMPLETED = {
        (Todo, 'Todo'),
        (InProgress, 'In Progress'),
        (AwaitingFeedback, 'Awaiting Feedback'),
        (Done, 'Done'),
    }

    name = models.CharField(max_length=100,
                            choices=COMPLETED,
                            default=Todo)

    def __str__(self):
        return f'({self.id}) {self.name}'


class Priority(models.Model):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'

    PRIORITIES = {
        (Low, 'Low'),
        (Medium, 'Medium'),
        (High, 'High'),
    }

    name = models.CharField(max_length=6,
                            choices=PRIORITIES,
                            default=Low)

    def __str__(self):
        return f'({self.id}) {self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.name}'


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    completed = models.ForeignKey(Completed, on_delete=models.SET_DEFAULT, default=1)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=3)
    priority = models.ForeignKey(Priority, on_delete=models.SET_DEFAULT, default=1)
    due_date = models.DateTimeField(default=django.utils.timezone.now)
    assigned_to = models.ManyToManyField(Contact, symmetrical=False, related_name='assigned_to')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.title}'
    

class Subtask(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'({self.id}) {self.title}'
