from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import math
#STATUS = ((0, 'Draft'), (1, 'Publish'))

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS = (
        ((0,'Draft' or 'draft')),((1,'Publish' or 'published'))
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now) #
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-publish',] #
    
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('post_detail', kwargs={'slug': str(self.slug)})

    def whenpublished(self):
        now = timezone.now()
        diff = now - self.publish
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str() +  'Just now'
            else:
                return str() + 'Few moments ago'
            
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str() + ' about a minute ago'
            else:
                return str(minutes) + ' muinutes ago'

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str() + ' about an hour ago'
            else:
                return str(hours) + ' hours ago'

        if diff.days >= 1 and diff.days < 2 :
            days = diff.days
            if days == 1:
                return str() + 'Yesterday'
            else:
                return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


    def whencreated(self):
        now = timezone.now()
        diff = now - self.created
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds
            if seconds == 1:
                return str() +  'Just now'
            else:
                return str() + 'Few seconds ago'
            
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes == 1:
                return str() + ' about a minute ago'
            else:
                return str(minutes) + ' muinutes ago'

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)
            if hours == 1:
                return str() + ' about an hour ago'
            else:
                return str(hours) + ' hours ago'

        if diff.days >= 1 and diff.days < 2 :
            days = diff.days
            if days == 1:
                return str() + 'Yesterday'
            else:
                return 'Comment {} by {}'.format(self.body, self.name)