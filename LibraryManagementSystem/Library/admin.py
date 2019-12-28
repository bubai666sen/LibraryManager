from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','publisher','year_of_publish']

class BookTransactionAdmin(admin.ModelAdmin):
    list_display = [ 'book','request_status','payment_status','created_by']

admin.site.register(Book,BookAdmin)
admin.site.register(BookTransaction,BookTransactionAdmin)