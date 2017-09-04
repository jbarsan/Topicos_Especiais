from django.db import models
from django.contrib.auth.models import User as UserDJ


# Create your models here.
class Geolocation(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        text = 'Lat: {} / Lng: {}'.format(self.lat, self.lng)
        return text


class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    geo = models.ForeignKey(Geolocation)

    def __str__(self):
        text = '{0}, {1}, {2}, {3}, {4}'.format(self.street, self.suite, self.city, self.zipcode, self.geo)
        return text


class User(models.Model):
    user = models.OneToOneField('auth.User', related_name='usuario')
    address = models.ForeignKey(Address)
    name = models.CharField(max_length=100)

    @property
    # username = models.CharField(max_length=100)
    def username(self):
        return self.user.username

    @property
    # email = models.EmailField()
    def email(self):
        return self.user.email

    @property
    def password(self):
        return self.user.password

    def __str__(self):
        text = '{0}, {1}'.format(self.name, self.email)
        return text


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        text = 'Postado: {0}, Título: {1}'.format(self.user.name, self.title)
        return text


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        text = 'Comentado por: {}'.format(self.name)
        return text
