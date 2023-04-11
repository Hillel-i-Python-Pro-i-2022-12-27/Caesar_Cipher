from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    message_encrypted = models.TextField(max_length=250)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages",
    )

    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    usage_count = models.IntegerField(default=0, blank=False, null=False)

    is_latest_mode_encrypted = models.BooleanField(default=True, blank=False, null=False)

    key = models.OneToOneField(
        "Key",
        on_delete=models.PROTECT,
        related_name="message",
    )

    def __str__(self):
        return f"Message {self.id} by {self.owner}. Usage count: {self.usage_count}."

    __repr__ = __str__

    class Meta:
        ordering = ["-modified_at"]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "message_encrypted",
                    "owner",
                    "key",
                ],
                name="unique_message_encrypted_with_key_per_owner",
            ),
        ]


class Key(models.Model):
    key_step = models.IntegerField(default=0, blank=True, null=True)
