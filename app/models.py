from django.db import models


class Todo(models.Model):
    Text=models.CharField(max_length= 200)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Text
