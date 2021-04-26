from django.db import models
from autoslug import AutoSlugField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(editable=True, populate_from='title', null=True, blank=True)
    added_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-date_added',)
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'


    
