from django.db import models


# Create your models here.


class XiaoShuo(models.Model):
    title = models.TextField()
    caption = models.TextField()
    detail = models.TextField()

    class Meta:
        db_table = 'xiaoshuo'
