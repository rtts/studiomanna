from django.db import models

class Event(models.Model):
    title = models.CharField('titel', max_length=32)
    date = models.DateField('datum')
    start_time = models.TimeField('begintijd', blank=True, null=True)
    end_time = models.TimeField('eindtijd', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'start_time']
