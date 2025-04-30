from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag

# show in the admin panel
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
