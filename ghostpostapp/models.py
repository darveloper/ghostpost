from django.db import models
from django.utils import timezone

class BR(models.Model):
    post = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    is_boast = models.BooleanField()

    def __str__(self):
        return self.post
    