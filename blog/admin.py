from django.contrib import admin

# Register your models here.python manage.py runserver
from .models import Post

admin.site.register(Post)