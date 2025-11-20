from django.db import models

from book_app.models import Book
    

class UserProfile(models.Model):

    username = models.CharField(max_length= 200)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)
    
class LoginTable(models.Model):

    username = models.CharField(max_length= 200)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    type = models.CharField(max_length= 200)

    def __str__(self):
        return '{}'.format(self.username)



from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"




class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)