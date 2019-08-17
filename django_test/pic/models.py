
from django.db import models
import os
import uuid
                #instance 表示的是Picture对象
def user_directory_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # return the whole path to the file
    #instance.user.username：用户主键，表示该用户单独的文件
    # 'content'  表示文章图片分类
    # str(instance.topic.id)  文章主键，表示某篇特定的文章的图片
    #图片的实际文件名
    return os.path.join(instance.user.username,'content',str(instance.topic.id),filename)
    #数据库存储最终的完整路径：用户id/文章目录/文章id/图片名
    #图片的时间路径为MEDIA_ROOT+数据库的路径


class User(models.Model):
    username=models.CharField('用户名',max_length=30,primary_key=True)


class Topic(models.Model):
    content=models.TextField('文章内容')
    username=models.ForeignKey(User,null=True)

class Picture(models.Model):
        topic = models.ForeignKey(Topic,null=True)
        user=models.ForeignKey(User,null=True)
        img = models.ImageField('图片', upload_to=user_directory_path)

