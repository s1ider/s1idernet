from django.db import models

class SearchHistory(models.Model):
    request = models.CharField(max_length=200)

    
  