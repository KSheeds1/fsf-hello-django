from django.db import models


class Item(models.Model):
    """
    Create Item model and define fields.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
