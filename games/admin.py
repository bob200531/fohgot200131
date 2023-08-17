from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Games)
# admin.site.register(Studio)
admin.site.register(PlayerAPI)
admin.site.register(Genre)
admin.site.register(GameCollection)

# class GameInline(admin.StackedInline):
#     model = Games


# @admin.register(Studio)
# class StudioAdmin(admin.ModelAdmin):
#     list_display = ['id','name','workers_count','games_count']
#     inlines = [GameInline]
