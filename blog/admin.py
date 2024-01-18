from django.contrib import admin
from .models import postModel,Comment


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
admin.site.register(postModel, PostModelAdmin,)
admin.site.register(Comment)