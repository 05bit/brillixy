from datetime import datetime
from django.db import models


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    published_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-published_at',)


class PostFile(models.Model):
    post = models.ForeignKey(Post)
    attachment = models.FileField(upload_to='attachments')

    def __unicode__(self):
        return self.attachment
