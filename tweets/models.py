from django.db import models

from common.models import CommonModel
from users.models import User


class Tweet(CommonModel):
    payload = models.TextField(max_length=180)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.payload


class Like(CommonModel):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} liked {self.tweet.id}"
