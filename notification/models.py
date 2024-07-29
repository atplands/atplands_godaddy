from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from post.models import Post


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, related_name="notification_post", null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_from_user" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_to_user" )
    notification_types = models.IntegerField(choices=NOTIFICATION_TYPES, null=True, blank=True)
    text_preview = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.text_preview



