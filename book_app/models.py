from django.db import models

# Create your models here.


#2. for foreign key working, we are going to add another model

class Author(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.name)
    


#this is the first model we created.
class Book(models.Model):

    title = models.CharField(max_length=200, null=True)

    price = models.IntegerField(null=True)

    image = models.ImageField(upload_to='book_media', null=True, blank=True)

    quantity = models.IntegerField(null= True)

    #to connec tthe author model to the book,we will use foreign key
    author = models.ForeignKey(Author, on_delete= models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.title)
