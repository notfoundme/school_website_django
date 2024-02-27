from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="course")

    def __str__(self):
        return self.title
    


class Testimonial(models.Model):
    name= models.CharField(max_length=255,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="testimonial")

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    name= models.CharField(max_length=255,null=False)
    image = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="news")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="News"



class Downloads(models.Model):
    title = models.CharField(max_length=255,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="downloads")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="Downloads"


class Contact(models.Model):
    name = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False)
    message = models.TextField()
    phoneNumber = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.name


    


