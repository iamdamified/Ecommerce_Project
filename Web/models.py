from django.db import models

# Create your models here.

class Hero(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_images')

    class Meta:
        verbose_name_plural = 'Heroes'

    def __str__(self):
        return self.category


class Hero_big(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='big_image')

    def __str__(self):
        return self.title
# this is for general products below:

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("KD", "Kids"),
        ("MN", "Men"),
        ("WM", "Women"),
        ("AC", "Accessories")
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=12)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
    

class Social(models.Model):
    image = models.ImageField(upload_to='socialmedia_images')
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name



# SUBJECT_CHOICES = (
#     ("I", "Inquiry"),
#     ("C", "Complaint")
# )
# This is for backend contact form
# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(choices=SUBJECT_CHOICES, max_length=3)
#     message = models.TextField()

#     def __str__(self):
#         return self.name
    

# # This is for frontend contact form
# class Contactinfo(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()


#     def __str__(self):
#         return self.name