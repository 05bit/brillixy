from datetime import datetime
from django.db import models
from django.core import urlresolvers


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    published_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-published_at',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return urlresolvers.reverse('admin:post_change', args=[self.pk])


class PostFile(models.Model):
    post = models.ForeignKey(Post)
    attachment = models.FileField(
        upload_to='attachments', help_text="Upload file size limit 2MB")

    def __unicode__(self):
        return unicode(self.attachment)

    def get_absolute_url(self):
        return self.attachment.url

