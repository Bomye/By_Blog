from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,
                               related_name="title",
                               on_delete=models.CASCADE)  # 映射关系 一个author可以对应多个博客    related_name：可以用博客名反向查找author
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)  # 规定BlogArticles对象的显示顺序是按照publish倒序

    def __str__(self):
        return self.title
