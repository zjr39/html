
from django.contrib import admin

from .models import Topic,Entry

# admin 用于管理后台相关操作的模块，site 是该模块中一个关键的对象，它管理着整个管理后台的各种配置和注册信息等。
# 当执行 admin.site.register(Topic) 操作时，就是告诉 Django 的管理后台，要把这个 Topic 模型纳入管理范围，
# 这样在访问 Django 管理后台的网页界面时，就可以对 Topic 模型对应的数据库表进行增删改查等操作了

admin.site.register(Topic)
admin.site.register(Entry)


#
# Register your models here.
