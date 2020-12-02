from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    post_time = models.TimeField()
    post_date = models.DateField()
    post_postedby = models.CharField(max_length=255)
    post_category = models.CharField(max_length=255)
    post_desc = models.TextField()

    def __str__(self):
        return self.post_title + " "+ "," + str(self.sno)

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name + " " + "-" + " " + str(self.email)