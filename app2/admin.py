from django.contrib import admin
from .models import post
admin.site.register(post)
from .models import blogcomment
admin.site.register(blogcomment)
# Register your models here.
