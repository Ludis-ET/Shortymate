from django.db import models
import uuid


class ShortenedURL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_unique_short_code()
        super().save(*args, **kwargs)

    def generate_unique_short_code(self):
        return str(uuid.uuid4())[:8]

    def __str__(self):
        return f"{self.short_code} => {self.long_url}"