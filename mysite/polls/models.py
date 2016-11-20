from django.db import models

# Create your models here.
SHORT_TEXT_LEN=1000



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=255) # title post
    datetime = models.DateTimeField(u'Date public') # date public
    content = models.TextField(max_length=10000) # text post

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/polls/%i/" % self.id

    def get_short_text(self):
        if len(self.content) > SHORT_TEXT_LEN:
            return self.content[:SHORT_TEXT_LEN]
        else:
            return self.content