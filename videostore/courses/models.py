from django.db import models

class Course(models.Model):
    slug = models.SlugField()#создание своего url
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='course_images')

    def __str__(self):
        return self.title