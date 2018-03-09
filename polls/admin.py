from django.contrib import admin

# Register your models here.
#once models are made, they need to be registered to view them on the admin page of the website
from .models import Question

admin.site.register(Question)