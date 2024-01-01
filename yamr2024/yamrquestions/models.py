import uuid as uuid_lib

from django.db import models
from django.conf import settings

from core.models import TimeStampedModel

class YamrQuestion(TimeStampedModel):
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="yamr_questions"
    )

    def __str__(self):
        return self.content


class YamrAnswer(TimeStampedModel):
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False)
    yamrbody = models.TextField()
    yamrquestion = models.ForeignKey(
        YamrQuestion, on_delete=models.CASCADE, related_name="yamr_answers"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="yamr_authored_answers"
    )
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="yamr_votes")

    def __str__(self):
        return self.author.username
