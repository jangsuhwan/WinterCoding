from django.db import models


class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=2)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' l ' + str(self.completed)

