from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

def save_topic_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = 'topic_pictures/{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    image = models.ImageField(upload_to=save_topic_image, blank=True, verbose_name='Topic Image')
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def save_lecture_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = 'lecture_files/{}/{}.{}'.format(instance.name, instance.name, ext)
        if os.path.exists(filename):
            new_name = str(instance.name) + str('1')
            filename =  'lecture_images/{}/{}.{}'.format(instance.name,new_name, ext)
    return os.path.join(upload_to, filename)

class Lecture(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name='lectures')
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name="Lecture no.")
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to=save_lecture_files,verbose_name="Video", blank=True, null=True)
    notes = models.FileField(upload_to=save_lecture_files,verbose_name="Notes", blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('curiculum:lecture_list', kwargs={'slug':self.topic.slug, 'course':self.Course.slug})
