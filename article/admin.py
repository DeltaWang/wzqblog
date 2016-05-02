from django.contrib import admin
from models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title','category','content')
    list_display = ['title','category','author']
    search_fields = ('title','author','category',)
    list_filter = ('category',)
    ordering = ['-publish_time',]


admin.site.register(Article,ArticleAdmin)