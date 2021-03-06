from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    STATUS = (
        ('Draft', 'D'),
        ('Published', 'P')
    )
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_header = models.ImageField(upload_to='images/image_headers', null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=9)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.strftime('%m'),
                             self.created.strftime('%d'),
                             self.slug])


