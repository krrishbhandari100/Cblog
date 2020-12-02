from django.contrib import admin
from blog.models import Post, Contact
# Register your models here.

@admin.register(Post)
class ModelAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)

admin.site.register(Contact)