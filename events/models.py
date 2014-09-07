from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField('timestamp')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)
