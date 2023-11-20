from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
       return self.reader_name

    reference_id=models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active=models.BooleanField(default=True)



from django.db import models

class books(models.Model):
    book_name = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.book_name
    






