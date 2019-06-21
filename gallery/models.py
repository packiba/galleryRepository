from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.urls import reverse

class Picture(models.Model):
    picture = models.ImageField(upload_to='media')
    title = models.CharField(max_length=60)
    created_date = models.DateTimeField(default=timezone.now)

    def get_name(self):
        directory = self.picture.name.split('/')
        return directory[-1]

    def image_tag(self):
        if self.picture:
            return mark_safe('<img width="200px" src="%s"/>' % self.picture.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
