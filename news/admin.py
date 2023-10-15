from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'country_code', 'author', 'published_on', 'created_on')
    list_filter = ('category', 'country_code', 'published_on', 'created_on')
    search_fields = ('title', 'author')


# Register the Article model with the custom admin class
admin.site.register(Article, ArticleAdmin)
