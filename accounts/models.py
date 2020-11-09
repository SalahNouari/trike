from django.db import models
from django.conf import settings

# Models
from logistics.models import OrderReview

# Custom User
from django.contrib.auth.models import UserManager, AbstractUser

class User(AbstractUser):
  # Additional fields
  facebook_id = models.CharField(max_length=25, blank=True, null=True)

  email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
  username = models.CharField(max_length=55, unique=True)
  contact = models.CharField(max_length=55, blank=True, null=True)
  gender = models.CharField(max_length=10, blank=True, null=True)
  picture = models.ImageField(upload_to='photos/profile_pictures/%Y/%m/%d/', blank=True, null=True)
  plate_number = models.CharField(max_length=55, unique=True, blank=True, null=True)

  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

  def __str__(self):
    return self.email

  @property
  def rider_rating(self):
    try:
      rating = normal_round(sum([int(review.rating) for review in OrderReview.objects.filter(order__rider=self)])/OrderReview.objects.filter(order__rider=self).count())
    except:
      rating = 0
    return rating


   
class Address(models.Model):
  # Basic Details
  user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)

  latitude = models.CharField(max_length=91)
  longitude = models.CharField(max_length=91)
  address = models.CharField(max_length=225)

  def __str__(self):
    return f'{self.user.email}'