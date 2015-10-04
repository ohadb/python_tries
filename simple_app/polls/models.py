import datetime
from django.utils import timezone

# Create your models here.
from django.db import models

class Question(models.Model):
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)