### 创建超级管理员

`python manage.py createsuperuser`
`http://127.0.0.1:8000/admin/` 登录admin站点

### APP应用配置

> 在apps.py 中配置

```python
from django.apps import AppConfig

class BooktestConfig(AppConfig):
    name = 'booktest'
    verbose_name = '图书管理'
```

> AppConfig.name 表示这个配置类是加载到哪个应用的，每个配置类必须包含此属性，默认自动生成
>
> AppConfig.verbose_name 用于设置该应用的直观可读的名字，此名字在Django提供的Admin管理站点中会显示

### 注册模型类

> 在应用的admin.py文件中注册

```python
from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
```

### 定义与使用Admin管理类

> Django提供的admin站点的展示下偶偶可以通过自定义ModeAdmin类来进行控制

```python
from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    pass
```

* 使用管理类的方式

  * 注册参数
    `admin.site.register(BookInfo, BookInfoAdmin)`

  * 装饰器

    ```python
    @admin.register(BookInfo)
    class BookInfoAdmin(admin.ModelAdmin):
        pass
    ```

### 调整列表页展示

1. 页大小
   `list_per_page = 2` 在admin管理类中定义每页显示的条目数，默认为100

2. 列表中的列
   `list_display = [模型字段1, 模型字段2]`  点击列头可以按指定字段的值进行排序

3. 将方法作为列

   ```python
   class BookInfo(models.Model):
       ...
       def pub_date(self):
           return self.bpub_date.strftime("%Y年%m月%d日")
       pub_date.short_description = '发布日期'
    	pub_date.admin_order_field = 'bpub_date' # 为方法指定排序的依据
       ...
       # 在admin管理类中设置
   	# list_display = ['id', 'btitle', 'pub_date']
   ```

   > 方法列是不能进行排序的，如果需要排序，就需要为方法指定排序的依据

   ​	`admin_order_field = 模型类字段`

4. 关联对象

   > 无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员

   ```python
   class HeroInfo(models.Model):
       ...
       def read(self):
   		return self.hbook.bread
       read.short_description = '图书阅读量'
       # list_display = ['read]
   ```

5. 右侧栏过滤器
   `list_filter = []` 只能接受字段，会将对应字段的值列出来，用于快速过滤，一般用于有重要值得字段

6. 搜索框

   `search_fields = []` 对指定的值进行搜索，支持模糊查询，列表类型，表示在这些字段上进行搜索。

### 调整编辑页展示

1. 显示字段
   `fields = []`  显示可编辑字段

2. 分组显示

   ```python
   fieldsets = (
   	('组1标题', ('fields': {'字段1', '字段2'})),
       ('组2标题', ('fields': {'字段3', '字段4'}))
   )
   ```

   ```python
   class BookInfoAdmin(admin.ModelAdmin):
       # fields = ['btitle', 'bpub_date'] # 修改时显示的字段
       # 分组显示
       fieldsets = (
           ('基本', {
               'fields': ['btitle', 'bpub_date', 'image']
           }),
           ('高级', {
               'fields': ['bread', 'bcomment'],
               'classes': ('collapse',)  # 是否折叠显示
           })
       )
   ```

3. 关联对象

   > 在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格，块两种

   * 类型InlineModelAdmin 表示在模型类的编辑页面嵌入关联模型的编辑
   * 子类TabularInline 以表格的形式嵌入
   * 子类StackedInline 以块的形式嵌入

   ```python
   class HeroInfoStackInline(admin.StackedInline):  #以表格嵌入继承admin.TabularInline
       model = HeroInfo # 要编辑的对象
       extra = 1 # 附加编辑的数量
   class BookInfoAdmin(admin.ModelAdmin):
       ...
       inlines = [HeroInfoStackInline]
   ```

### 调整站点信息

```python
admin.site.site_header = '网站页头'
admin.site.site_title = '页面标题'
admin。site.index_title = '首页标语'
```

### 上传图片

> Django提供文件系统的支持，在Admin站点中可以轻松上传图片

​	`pip install Pillow` 安装所需包

1. 配置
   `MEDIA_ROOT = os.path.join(BASE_DIR, 'static_files/media')`

2. 为模型类添加ImageField字段

   ```python
   class BookInfo(models.Model):
       ...
       image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)
   ```

   - upload_to 选项指明该字段的图片保存在MEDIA_ROOT目录中的哪个子目录

   - ```python
     python manage.py makemigrations
     python manage.py migrate
     ```


