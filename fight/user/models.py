from django.db import models

# Create your models here.


class CCharFiled(models.Field):

    '''
    新建一个字段类表示char属性
    '''

    def __init__(self,max_length,*args,**kwargs):
        self.max_length=max_length
        super(CCharFiled,self).__init__(max_length=self.max_length,*args,**kwargs)

    def db_type(self, connection):
        '''

        :param connection:
        :return:
        '''
        return 'char(%s)'%(
            self.max_length
        )

class User(models.Model):
    username=models.CharField(max_length=20)
    pwd=CCharFiled(max_length=20)