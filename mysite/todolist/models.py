from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=2)

    class Meta:
        ordering = ["-priority", "title"]

    def __str__(self):
        return self.title

