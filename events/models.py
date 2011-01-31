from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

def today():
    now = datetime.now()
    start = datetime.min.replace(year=now.year, month=now.month,
                                day=now.day)
    end = (start + timedelta(days=1)) - timedelta.resolution
    return (start, end)

class EventQuerySet(QuerySet):
    def today(self):
        return self.filter(creation_date__range=today())

class EventManager(models.Manager):
    
    def get_query_set(self):
        return EventQuerySet(self.model)
    
    def today(self):
        return self.get_query_set().today()

# Create your models here.
class Event(models.Model):
    description = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, related_name= 'event_creator_set')
    attendees = models.ManyToManyField(User, through="Attendance")
    latest = models.BooleanField(default=True)
    
    objects = EventManager()
    
    def __unicode__(self):
        return self.description
    
    def save(self, **kwargs):
        Event.objects.filter(latest=True,
            creator=self.creator).today().update(latest=False)
        super(Event, self).save(**kwargs)
        
class Attendance(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    registration_date = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return "%s is attending %s"%(self.user.username, self.event)
    
    class Meta(object):
        verbose_name_plural = "Attendance"