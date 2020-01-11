from django.contrib import admin

# our imported classes

from . models import author, post 

# Register your models here.
admin.site.register(author)
admin.site.register(post)
