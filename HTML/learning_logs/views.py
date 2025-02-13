from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm
# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有主题"""
    # 从数据库中获取所有的Topic模型实例，并按照时间升序排列
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题"""
    # request.method是request对象的一个属性，用于获取 HTTP 请求的方法类型(GET,POST,PUT,DELETE)
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            # new_topic = form.save(commit=False)
            # new_topic.owner = request.user
            new_topic.save()
            # redirect 用于表单提交成功后跳转页面、用户权限验证后跳转到相应页面等场景。
            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)