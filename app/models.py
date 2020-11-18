from django.db import models


class Person(models.Model):
    """
    A person instance (FOP/OP)
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True)
    ico = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return self.name