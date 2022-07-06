from django.db import models


class Card(models.Model):
    quest = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.quest