from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogArticles  # 将BlogArticles类引入到当前文件夹


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)  # 将BlogArticles类注册到admin
