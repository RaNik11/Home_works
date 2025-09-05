from django.db import models

STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In progress"),
        ("pending", "Pending"),
        ("blocked", "Blocked"),
        ("done", "Done"),
    ]


class Task(models.Model):

    title = models.CharField(max_length=100, verbose_name = "Название")
    descriprion = models.TextField(blank=True, verbose_name= "Описание", null=True)
    category = models.ManyToManyField("Category", related_name="Категория")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,verbose_name= "Статус", default="new")
    deadline = models.DateTimeField(verbose_name= "Дата и время дэдлайна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Дата и время создания",)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=255, verbose_name = "Название")
    description = models.TextField( verbose_name= "Описание", blank=True, null=True)
    task = models.ForeignKey("Task", related_name="subtasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, verbose_name= " Статус задачи", choices=STATUS_CHOICES, default="new")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
