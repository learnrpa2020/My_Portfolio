from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    img=models.ImageField(upload_to='portfolio_app/images')
    url=models.URLField(blank=True)


    def __str__(self):
        return self.title
