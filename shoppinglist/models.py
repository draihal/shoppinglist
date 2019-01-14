from django.db import models
from django.conf import settings


class Shoppinglist(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    shoppinglist_item = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.shoppinglist_item
        else:
            return self.shoppinglist_item
