from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    book_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50,null=True, blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    version = models.CharField(max_length=30,null=True, blank=True)
    year_of_publish = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=30,null=True, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='uploads/books/')
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #updated_by = models.ForeignKey(User, related_name='updated_by_user_book',null=True,on_delete=models.SET_NULL,default='auth.User')
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.title + ' (' +self.book_id+ ')'

class BookTransaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    STATUS = [
        ('Requested', 'Requested'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Returned', 'Returned'),
        ('Return Rejected', 'Return Rejected'),
    ]
    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('N/A', 'N/A'),
    ]
    request_status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='Requested'
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS,
        default='N/A'
    )
    fine = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
    comments = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User, related_name='created_by_user' ,on_delete=models.CASCADE)
    #updated_by = models.ForeignKey(User, related_name='updated_by_user',null=True,on_delete=models.SET_NULL,default='auth.User')
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.book.title + ' (' +self.transaction_id+ ')'