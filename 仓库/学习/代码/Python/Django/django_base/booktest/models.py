from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书模型类"""

    btitle = models.CharField(max_length=20, verbose_name='书名')
    bpub_date = models.DateField(verbose_name='出版日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    image = models.ImageField(upload_to='booktest', verbose_name='图书封面', null=True)

    class Meta:
        # 数据库表名
        db_table = 'tb_books'

        # admin站点中显示的名称
        verbose_name = '图书'

        # admin站点中显示的复数名称
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个对象的显示信息"""

        return self.btitle


class HeroInfo(models.Model):
    """英雄模型类"""

    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )

    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 外键  1 : m 多方
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:

        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname




# 多对多关系模型

class TypeInfo(models.Model):
    """创建新闻分类模型"""
    tname = models.CharField(max_length=20)
    def __str__(self):
        return self.tname

class NewsInfo(models.Model):
    """
    新闻内容模型类
    bookinfo_newsinfo
    """
    ntitle = models.CharField(max_length=20)
    npub_date = models.DateTimeField(auto_now_add=True)
    ncontent = models.FileField()
    # 建立多对多关系
    ntype = models.ManyToManyField('TypeInfo')

    def __str__(self):
        return self.ntitle



# 一对一模型
class  Student(models.Model):
    """学生模型类"""
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname

class StuInfo(models.Model):
    """学生简历模型类"""
    scontent = models.CharField(max_length=200)
    stu = models.OneToOneField('Student')
    def __str__(self):
        return self.scontent


# 自关联一对多模型
class  AreaInfo(models.Model):
    """
    地区模型类
    booktest_areainfo

    """

    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle



# 自关联多对多
class User(models.Model):
    """用户模型"""
    name = models.CharField(max_length=20, unique=True)

    # 用户所有的粉丝
    followers = models.ManyToManyField('self')

    def __str__(self):
        return self.name

