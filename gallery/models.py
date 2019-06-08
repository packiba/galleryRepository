from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField

class Picture(models.Model):
    picture = models.ImageField(upload_to='static')
    title = models.CharField(max_length=60)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_date',)


    def __str__(self):
        return self.title



