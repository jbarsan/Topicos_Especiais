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
    user = models.OneToOneField(UserDJ)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=16, default='password123')
    address = models.ForeignKey(Address)

    def __str__(self):
        text = '{0}, {1}, {2}'.format(self.username, self.name, self.email)
        return text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            cadastro = User.objects.filter(username=self.username).count()
            if cadastro:
                print('Usuário já cadastrado')

            usuario = UserDJ.objects.filter(username=self.username)
            if usuario:
                usr = usuario[0]
            else:
                usr = UserDJ.objects.create_user(self.username, self.email, self.password)
            usr.save()
            self.user = usr
        else:
            self.user.username = self.username
            self.user.email = self.email
            self.user.set_password(self.password)
            self.user.save()

        super(User, self).save()


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
