from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Games)
admin.site.register(Studio)
admin.site.register(PlayerAPI)
admin.site.register(Genre)