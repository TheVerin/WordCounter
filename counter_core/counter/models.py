from django.db import models


class WoCount(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    number = models.IntegerField(default=00000)

    class Meta:
        db_table = 'counter'

    def __str__(self):
        return self.title
