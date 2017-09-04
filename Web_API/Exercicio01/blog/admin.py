from django.contrib import admin
from blog.models import *


# Register your models here.
admin.site.register(Geolocation)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)