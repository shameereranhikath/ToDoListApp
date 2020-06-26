from django.db import models


# Create your models here.

class Todolist(models.Model):
    list_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField()
    text = models.CharField(max_length=2048)

    def __str__(self):
        return self.text
