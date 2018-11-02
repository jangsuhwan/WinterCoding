from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'priority', 'due_date', 'completed']

admin.site.register(List, ListAdmin)
