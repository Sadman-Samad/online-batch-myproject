from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to="banner/image")
    description = models.TextField()
    

class StudentInformation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    st_id = models.IntegerField()
    email = models.EmailField()
    subject = models.IntegerField()    


class Product(models.Model):
    PRODUCT_COLOR = (
        ('RED','RED'),
        ('BLUE','BLUE'),
        ('YELLOW','YELLOW'),

    )
    title = models.CharField(max_length=250) 
    slug = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='image/')
    color = models.CharField(max_length=250, choices=PRODUCT_COLOR)

    def __str__(self):
        return f"id-{self.id}-{self.title}" 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.color)
        super(Product, self).save(*args, **kwargs)
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.TextField()

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'category')

    date = models.DateTimeField()

    def __str__(self):
        return self.name

