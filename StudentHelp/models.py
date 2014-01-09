from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=80)
    finnish_translate = models.CharField(max_length=80)

    def get_translation(self):
        ""
        return self.finnish_translate

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.word