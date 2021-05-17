from django.db import models

def upload_post_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['posts', str(instance.Blog.id)+str(instance.title)+str(".")+str(ext)])

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True, upload_to=upload_post_path)
    text = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
