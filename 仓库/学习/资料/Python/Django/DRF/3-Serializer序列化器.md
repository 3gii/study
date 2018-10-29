#### 序列化器的作用

1. 序列化
   * 将实例对象转化为字典数据
2. 反序列化
   * 数据校验
   * 数据保存（新增或更新）

#### 定义Serializer

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
```

> **serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。**serializer是独立于数据库之外的存在。

#### 字段与选项

1. 选用字段类型：

   | 字段                    | 字段构造方式                                                 |
   | ----------------------- | ------------------------------------------------------------ |
   | **BooleanField**        | BooleanField()                                               |
   | **NullBooleanField**    | NullBooleanField()                                           |
   | **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True) |
   | **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank=False) |
   | **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
   | **SlugField**           | SlugField(max_length=50, min*length=None, allow_blank=False) 正则字段，验证正则模式 [-a-zA-Z0-9*-]+ |
   | **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
   | **UUIDField**           | UUIDField(format='hex_verbose')  format:  1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"`  2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"`  3）`'int'` - 如: `"123456789012312313134124512351145145114"`  4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
   | **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
   | **IntegerField**        | IntegerField(max_value=None, min_value=None)                 |
   | **FloatField**          | FloatField(max_value=None, min_value=None)                   |
   | **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None) max_digits: 最多位数 decimal_palces: 小数点位置 |
   | **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
   | **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
   | **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
   | **DurationField**       | DurationField()                                              |
   | **ChoiceField**         | ChoiceField(choices) choices与Django的用法相同               |
   | **MultipleChoiceField** | MultipleChoiceField(choices)                                 |
   | **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
   | **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
   | **ListField**           | ListField(child=, min_length=None, max_length=None)          |
   | **DictField**           | DictField(child=)                                            |

2. 选项参数

   | 参数名称            | 作用             |
   | ------------------- | ---------------- |
   | **max_length**      | 最大长度         |
   | **min_length**      | 最小长度         |
   | **allow_blank**     | 是否允许为空     |
   | **trim_whitespace** | 是否截断空白字符 |
   | **max_value**       | 最大值           |
   | **min_value**       | 最小值           |

3. 通用参数

   | 参数名称           | 说明                                          |
   | ------------------ | --------------------------------------------- |
   | **read_only**      | 表明该字段仅用于序列化输出，默认False         |
   | **write_only**     | 表明该字段仅用于反序列化输入，默认False       |
   | **required**       | 表明该字段在反序列化时必须输入，默认True      |
   | **default**        | 序列化和反序列化时使用的默认值                |
   | **allow_null**     | 表明该字段是否允许传入None，默认False         |
   | **validators**     | 该字段使用的验证器                            |
   | **error_messages** | 包含错误编号与错误信息的字典                  |
   | **label**          | 用于HTML展示API页面时，显示的字段名称         |
   | **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |

#### 创建Serializer对象

`Serializer(instance=None, data=empty, **kwargs)`

1）用于序列化时，将模型类对象传入**instance**参数

2）用于反序列化时，将要被反序列化的数据传入**data**参数

3）除了instance和data参数外，在构造Serializer对象时，还可通过**context**参数额外添加数据

#### 序列化器的使用

```python
book = BookInfo.objects.get(id=2)
    serializer = BookInfoSerializer(book)
    book = serializer.data
    print(book)
```

```python
class User(object):
    """用户类"""

    def __init__(self, name, age, gender, addr):

        self.name = name
        self.age = age
        self.gender = gender
        self.addr = addr
        
        
 class UserSerializer(serializers.Serializer):
    """用户序列化器类"""

    GENDER_CHOICE = (
        (0, '男'),
        (1, '女')
    )
    name = serializers.CharField(label='姓名',
                                 max_length=20,
                                 min_length=5,
                                 error_messages={
                                     'max_length': '最大长度不能超过20',
                                     'min_length': '最小长度不能少于5'
                                 },
                                 help_text='html帮助提示信息')
    age = serializers.IntegerField(label='年龄')
    gender = serializers.ChoiceField(choices=GENDER_CHOICE, default=0)
    addr = serializers.CharField(default='默认地址')  
    
if __name__ == '__main__':

    # ==========
    # 序列化操作
    # ==========
    user = User('张国鹏', 18, '男', '北京')
    serializer1 = UserSerializer(user)
    # 序列化后的数据
    print(serializer1.data)
```



#### 关联对象嵌套序列化

```python
class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    id = serializers.IntegerField(label='ID',  read_only=True)
    hname = serializers.CharField(label='名字',max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
```

1. PrimaryKeyRelatedField

   ```python
    # PrimaryKeyRelatedField
       hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
       # 或
       hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
   ```

   > 指明字段时需要包含read_only=True或者queryset参数：
   >
   >`hbook`等于关联表主键
   >
   > - 包含read_only=True参数时，该字段将不能用作反序列化使用
   > - 包含queryset参数时，将被用作反序列化时参数校验使用

2. 使用关联对象的序列化器
   `hbook = BookInfoSerializer()`

3. StringRelatedField

   `hbook = serializers.StringRelatedField(label='图书')`  \__str__返回的值

4. many参数

   > 如果关联对象不只一个时，需要改参数

   ```python
   class BookInfoSerializer(serializers.Serializer):
       """图书数据序列化器"""
   	...
       serializers.PrimaryKeyRelatedField(read_only=True, many=True)
   ```

#### 反序列化

1. 验证
   使用序列化器进行反序列化时，需要对数据进行验证后，才能获取验证成功的数据或保存成模型类对象。

   在获取反序列化的数据前，必须调用**is_valid()**方法进行验证，验证成功返回True，否则返回False。

   验证失败，可以通过序列化器对象的**errors**属性获取错误信息，返回字典，包含了字段和字段的错误。如果是非字段错误，可以通过修改REST framework配置中的**NON_FIELD_ERRORS_KEY**来控制错误字典中的键名。

   验证成功，可以通过序列化器对象的**validated_data**属性获取数据。

   在定义序列化器时，指明每个字段的序列化类型和选项参数，本身就是一种验证行为。

   ```python
   data = {'bpub_date': 123}
   serializer = BookInfoSerializer(data=data)
   serializer.is_valid()  # 返回False
   serializer.errors
   # {'btitle': [ErrorDetail(string='This field is required.', code='required')], 'bpub_date': [ErrorDetail(string='Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]].', code='invalid')]}
   serializer.validated_data  # {}
   
   data = {'btitle': 'python'}
   serializer = BookInfoSerializer(data=data)
   serializer.is_valid()  # True
   serializer.errors  # {}
   serializer.validated_data  #  OrderedDict([('btitle', 'python')])
   ```

   is_valid()方法还可以在验证失败时抛出异常serializers.ValidationError，可以通过传递**raise_exception=True**参数开启，REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应。
   `serializer.is_valid(raise_exception=True)`  # Return a 400 response if the data was invalid.

2. 定义验证行为

   * validators

     ```python
     def about_django(value):
         if 'django' not in value.lower():
             raise serializers.ValidationError("图书不是关于Django的")
         return value
             
     class BookInfoSerializer(serializers.Serializer):
     	    btitle = serializers.CharField(label='名称', max_length=20, validators=[about_django])
     
     ```

   * validate_<field_name>

     ```python
     # <field_name> 需要验证的字段
     class BookInfoSerializer(serializers.Serializer):
         """图书数据序列化器"""
         ...
     
         def validate_btitle(self, value):
             if 'django' not in value.lower():
                 raise serializers.ValidationError("图书不是关于Django的")
             return value
     ```

   * validate

     ```python
     # 多字段比较验证
     class BookInfoSerializer(serializers.Serializer):
         """图书数据序列化器"""
         ...
     
         def validate(self, attrs):
             bread = attrs['bread']
             bcomment = attrs['bcomment']
             if bread < bcomment:
                 raise serializers.ValidationError('阅读量小于评论量')
             return attrs
     ```

3. 保存

   ```python
   class BookInfoSerializer(serializers.Serializer):
       """图书数据序列化器"""
       ...
   
       def create(self, validated_data):
           """新建"""
           return BookInfo(**validated_data)
   
       def update(self, instance, validated_data):
           """更新，instance为要更新的对象实例"""
           instance.btitle = validated_data.get('btitle', instance.btitle)
           instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
           instance.bread = validated_data.get('bread', instance.bread)
           instance.bcomment = validated_data.get('bcomment', instance.bcomment)
           return instance
   ```

   ```python
   # 如果需要在返回数据对象的时候，也将数据保存到数据库中
   class BookInfoSerializer(serializers.Serializer):
       """图书数据序列化器"""
       ...
   
       def create(self, validated_data):
           """新建"""
           return BookInfo.objects.create(**validated_data)
   
       def update(self, instance, validated_data):
           """更新，instance为要更新的对象实例"""
           instance.btitle = validated_data.get('btitle', instance.btitle)
           instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
           instance.bread = validated_data.get('bread', instance.bread)
           instance.bcomment = validated_data.get('bcomment', instance.bcomment)
           instance.save()
           return instance
   ```

   > 实现了上述两个方法后，在反序列化数据的时候，就可以通过save()方法返回一个数据对象实例了

   ```python
   book = serializer.save()
   ```

   > 如果创建序列化器对象的时候，没有传递instance实例，则调用save()方法的时候，create()被调用，相反，如果传递了instance实例，则调用save()方法的时候，update()被调用。

   ```python
      	# 如果使用第一种保存方式不会对数据库操作
       data = {'btitle': '封神演义'}
       serializer = BookInfoSerializer(data=data)
       valid = serializer.is_valid()  # True
       s = serializer.save()  # <BookInfo: 封神演义>
   
   
       book = BookInfo.objects.get(id=2)
       data = {'btitle': '倚天剑'}
       serializer = BookInfoSerializer(book, data=data)
       v = serializer.is_valid()  # True
       s = serializer.save()  # <BookInfo: 倚天剑>
       b = book.btitle  # '倚天剑'
   ```

   * 说明

     1） 在对序列化器进行save()保存时，可以额外传递数据，这些数据可以在create()和update()中的validated_data参数获取到

     ```python
     serializer.save(owner=request.user)
     ```

     2）默认序列化器必须传递所有required的字段，否则会抛出验证异常。但是我们可以使用partial参数来允许部分字段更新

     ```python
     # Update `comment` with partial data
     serializer = CommentSerializer(comment, data={'content': u'foo bar'}, partial=True)
     ```

#### 模型类序列化器

> 模型序列化器类已经实现了create方法和update方法，并且在返回对象时已经进行了数据保存

1. 定义

   ```python
   class BookInfoSerializer(serializers.ModelSerializer):
       """图书数据序列化器"""
       class Meta:
           model = BookInfo
           fields = '__all__'
   ```

   * model 指明参照哪个模型
   * fields 指明为模型类的哪些字段生成

2. 指定字段

   * fields 显示字段

     ```python
     class BookInfoSerializer(serializers.ModelSerializer):
         """图书数据序列化器"""
         class Meta:
             model = BookInfo
             fields = ('id', 'btitle', 'bpub_date')  # '__all__' 表示全部字段
     ```

   * exclude 排除字段

   * 默认ModelSerializer使用主键作为关联字段，但是我们可以使用**depth**来简单的生成嵌套表示，depth应该是整数，表明嵌套的层级数量

     ```python
     class HeroInfoSerializer2(serializers.ModelSerializer):
         class Meta:
             model = HeroInfo
             fields = '__all__'
             depth = 1
     ```

     形成的序列化器

     ```python
     HeroInfoSerializer():
         id = IntegerField(label='ID', read_only=True)
         hname = CharField(label='名称', max_length=20)
         hgender = ChoiceField(choices=((0, 'male'), (1, 'female')), label='性别', required=False, validators=[<django.core.valators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
         hcomment = CharField(allow_null=True, label='描述信息', max_length=200, required=False)
         hbook = NestedSerializer(read_only=True):
             id = IntegerField(label='ID', read_only=True)
             btitle = CharField(label='名称', max_length=20)
             bpub_date = DateField(allow_null=True, label='发布日期', required=False)
             bread = IntegerField(label='阅读量', max_value=2147483647, min_value=-2147483648, required=False)
             bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=-2147483648, required=False)
             image = ImageField(allow_null=True, label='图片', max_length=100, required=False)
     ```

   * 指明只读字段

     ```python
     class BookInfoSerializer(serializers.ModelSerializer):
         """图书数据序列化器"""
         class Meta:
             model = BookInfo
             fields = ('id', 'btitle', 'bpub_date'， 'bread', 'bcomment')
             read_only_fields = ('id', 'bread', 'bcomment')
     ```

3. 添加额外参数

   > 可以使用**extra_kwargs**参数为ModelSerializer添加或修改原有的选项参数

   ```python
   class BookInfoSerializer(serializers.ModelSerializer):
       """图书数据序列化器"""
       class Meta:
           model = BookInfo
           fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
           extra_kwargs = {
               'bread': {'min_value': 0, 'required': True},
               'bcomment': {'min_value': 0, 'required': True},
           }
   
   # BookInfoSerializer():
   #    id = IntegerField(label='ID', read_only=True)
   #    btitle = CharField(label='名称', max_length=20)
   #    bpub_date = DateField(allow_null=True, label='发布日期', required=False)
   #    bread = IntegerField(label='阅读量', max_value=2147483647, min_value=0, required=True)
   #    bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=0, required=True)
   ```