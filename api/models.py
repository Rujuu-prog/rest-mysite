from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify 

def upload_post_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['posts', str(instance.id)+str(instance.title)+str(".")+str(ext)])

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    text = models.CharField(max_length=30)
    main_text = MarkdownxField('本文')
    is_public = models.BooleanField('公開する', default=False)
    create_on = models.DateTimeField(auto_now_add=True)

    def convert_markdown_to_html(self):
        return markdownify(self.main_text)

    def __str__(self):
        return self.title
