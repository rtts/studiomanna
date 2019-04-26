from django.db import models

TYPES = [
    (1, 'Yogales'),
    (2, 'Shared dinner'),
    (3, 'Workshop'),
]

class Event(models.Model):
    title = models.CharField('titel', max_length=32)
    type = models.PositiveIntegerField('type', choices=TYPES)
    date = models.DateField('datum')
    start_time = models.TimeField('begintijd', blank=True, null=True)
    end_time = models.TimeField('eindtijd', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'start_time']
