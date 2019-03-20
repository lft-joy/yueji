from django.db import models


# Create your models here.


class Cmdb(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='标题', max_length=50)

    def __str__(self):          #这个方法的作用是将你输入的title设置为标题
        return self.title
