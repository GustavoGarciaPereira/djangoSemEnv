from django.db import models
from django.contrib import admin
# Create your models here.


class BlogPast(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	time = models.DateTimeField()

class BlogPostAdim(admin.ModelAdmin):
	list_display = ('title','time')



admin.site.register(BlogPast,BlogPostAdim)


