"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include

# urlpatterns 是一个包含路由规则的列表
urlpatterns = [
    # 第一个路由将以 “admin/” 开头的 URL 路由到 Django 的管理后台的 URL 配置。(http://example.com/admin/)
    path('admin/', admin.site.urls),
    # 第二个路由将根路径（空字符串）路由到名为 “learning_logs.urls” 模块中的 URL 配置。
    # include函数允许将 URL 路由规则分散到不同的模块中，这样每个应用可以有自己独立的urls.py文件来定义和管理它自己的路由规则。
    path('', include('learning_logs.urls')),
]
