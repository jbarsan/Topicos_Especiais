from django.db import models


# Create your models here.
class Geolocation(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        text = 'Lat: {}' \
               'Lng: {}'.format(self.lat, self.lng)
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
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.ForeignKey(Address)

    def __str__(self):
        text = '{0}, {1}, {2}'.format(self.username, self.name, self.email)
        return text


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        text = 'Postado: {0}, Título: {1}'.format(self.user.name, self.title)
        return text


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        text = 'Comentado por: {}'.format(self.name)
        return text