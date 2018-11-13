from django.contrib import admin
from cms.models import Article, Category, Tag, AdImages

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    # 显示中文名称
    list_display = (
        'id',
        'title',
        'author',
        'views',
        'category',
        'create_time',
        'last_modified_time',
        'topped',
        'status',
    )

    # 可以搜索的字段
    search_fields = (
        'title',
        'author__username',
        'content', 'status',
        'category__name',
        'tags__name',
    )

    # 分页
    list_per_page = 10

    # 默认可编辑字段
    list_editable = ['status', 'category', 'topped', ]

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title',)

    # 过滤器
    list_filter =('category', 'status', 'author',)

    # 用于颜色显示
    # def color_status(self):
    #     if self.status == 'Draft':
    #         colo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'last_modified_time')
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class AdImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'index', 'add_time',)
    list_editable = ['image', 'url', 'index', ]


class ThisAdminSite(admin.AdminSite):
    site_header = 'SimpleCMS 内容管理系统'
    site_title = 'SimpleCMS 内容管理系统'  # 此处设置页面头部标题


admin.site = ThisAdminSite(name='admin')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AdImages, AdImageAdmin)
