from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class reader(models.Model):
    reference_id=models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active=models.BooleanField(default=True)

    def _str_(self):
       return self.reader_name

class books(models.Model): 
    book_name = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='books/', null=True, blank=True)

    def _str_(self):
        return self.book_name
    

class mybag(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(books, null=True, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
STATUS_CHOICES = (
    ("Returned", "Returned"),
    ("Not Returned", "Not Returned"),
)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
    return_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Not Returned")

    def _str_(self):
        return self.user.username + 's order'
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)

    def _str_(self):
        return self.user.username + 's wishlist'