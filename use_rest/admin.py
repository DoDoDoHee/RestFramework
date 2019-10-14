from django.contrib import admin
from .models import Blog, BlogPic, BlogFile
# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogPic)
admin.site.register(BlogFile)