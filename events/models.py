from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField('timestamp')

    def __unicode__(self):
        return self.location

    class Meta:
        ordering = ('timestamp',)
