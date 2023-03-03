from django.views.generic import ListView
from .models import PersonInfo
class index(ListView):
    # 设置模板文件
    template_name = 'index.html'
    # 设置模型外的数据
    extra_context = {'title': '人员信息表'}
    # 查询模型PersonInfo
    queryset = PersonInfo.objects.all().order_by('id')
    # 每页显示一条数据
    paginate_by = 1
    # 若不设置，则模板上下文默认为PersonInfo_list
    # context_object_name = 'Personinfo'