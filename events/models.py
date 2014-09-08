from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    user = models.ForeignKey(User, related_name="locations")
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    lat = models.CharField(max_length=32)
    lon = models.CharField(max_length=32)
    timestamp = models.DateTimeField('timestamp')

    def __unicode__(self):
        return '%s, %s' % (self.city, self.state)

    class Meta:
        ordering = ('-timestamp',)
