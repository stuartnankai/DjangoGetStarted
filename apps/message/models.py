# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 继承于django.db.models.Model
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, max_length=50,default="", verbose_name="Primary key")
    # 设置最大长度，verbose_name在后台显示字段会用到
    name = models.CharField(max_length=20,null=True,blank=True,default="", verbose_name=u"Username")
    # Django提供内置的邮箱字段会帮忙验证` default_validators = [validators.validate_email]`
    email = models.EmailField(verbose_name=u"Email")
    address = models.CharField(max_length=100, verbose_name=u"Address")
    message = models.CharField(max_length=500, verbose_name=u"Message")

    class Meta:
        verbose_name = u"Message"

        # 指明复数信息，否则后台显示"用户留言s"
        verbose_name_plural = verbose_name

        # 这里我们让它自动生成所以不用指定db-table
        # db_table = user_message

        # ordering指定默认排序字段,如：
        # ordering = ['-object_id']
