from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.location = self.location.lower()
        return super(Person, self).save(*args, **kwargs)
