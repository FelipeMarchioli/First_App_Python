from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200, default='', help_text='Enter with a book title')
  image = models.ImageField(max_length=300, default='', help_text='Select a book cover')  
  author = models.CharField(max_length=100, default='', help_text='Enter with a book author')
  headquarter = models.CharField(max_length=100, default='', help_text='Enter with your headquarter')
  deleted = models.BooleanField(default=False)
  pages = models.IntegerField(default=0, help_text='Enter with a total of pages')
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title