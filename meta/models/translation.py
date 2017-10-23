# third-party
from django.contrib.auth.models import User
from django.db import models

# local
from meta.models.song import Song


class Translation(models.Model):
    TAILO = 'TL'
    HANZI = 'HZ'
    LANG_CHOICES = (
        (TAILO, '全羅'),
        (HANZI, '全漢'),
    )

    song = models.ForeignKey(Song)
    line_no = models.PositiveSmallIntegerField()
    lang = models.CharField(
        max_length=2,
        choices=LANG_CHOICES)
    content = models.CharField(max_length=1000)
    contributor = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
