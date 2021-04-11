from django.db import models

class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title
