from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.

CATEGORY_CHOICES = [
	(1,'Car-Owner'),
	(2,'Mechanic/Garage'),
	(3,'Spare Parts Retailer'),	
] 

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = CloudinaryField('image')
    description = models.CharField(max_length=250)
    mobile_number = models.IntegerField(blank=True)
    email =  models.CharField(max_length=60) 
    category = models.SmallIntegerField(choices=CATEGORY_CHOICES, default="")
    


class Post(models.Model):
    poster = models.ForeignKey(User,on_delete = models.CASCADE)
    issue = HTMLField()
    issue_picture = CloudinaryField('image')

class Response(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    responses = HTMLField()
    
class Advice(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    advice = HTMLField()
        