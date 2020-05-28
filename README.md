# 总体介绍
本Repository中包含3个项目，项目使用的技术、主要功能、图形界面展示如下：

# 1.dataset_tools图片集处理工具

![image](https://github.com/AprilJW/images/blob/master/dataset_tools.png)

+ 使用python+Qt/html实现

+ 主要功能有：
  + 图片展示，可以展示xml 、json 、voc、 coco等格式数据；
  + 检查标注数据正确性，统一修改标注label；
  + 图片格式化，格式化成voc coco等格式；
  + resize图片，将图片缩放成指定大小的尺寸；
  + 倍增图片，通过旋转、平移、复制、增加对比度，可以将几十张图片倍增成几十万张图片，满足深度学习训练要求；
  + merge图片集，可以合并任意数量文件夹图片；
  + 各种其他小功能。

+ 展示图片样例
![image](https://github.com/AprilJW/images/blob/master/dataset_mast.png)
+ dataset_tools前端改写成html界面
![image](https://github.com/AprilJW/images/blob/master/data_tools_html.png)

# 2. 2D_data_Preprocessing图片预处理工具

![image](https://github.com/AprilJW/images/blob/master/2d_data.png)

+ 使用python + QT实现
+ 主要功能：
  + 加载标注文件夹，并将图片解析成对应的label和items；
  + 针对提取出的items加相应的算法，如背景color_bg, file_bg, Resize, Rotation,Move,Shaow等；
  + 生成配置文件，将界面上的填写的生成数据参数，保存到配置文件中，下次生成可以直接加载配置文件，生成相同数据，相当原始训练数据的备份；
  + 生成2D虚拟数据，解决标注图片数量少成本高的问题。
  
+ 原始标注图片样例
![image](https://github.com/AprilJW/images/blob/master/2d_data_origin.png)
+ 生成虚拟图片样例
![image](https://github.com/AprilJW/images/blob/master/2d_data_gene.png)

# 3. ihome_python爱家租房项目

- 项目工具：
  python +  flask + mysql + redis + nginx

- 主要功能：

  - 用户模块，用户注册，完成手机号、短信验证、密码确认等功能。短信验证之前需要确保用户没有注册过，生成的短信验证码先保存在redis中，然后通过celery方式发送给用户，注册成功后，会采用手机号作为唯一键的方式，将用户信息保存在mysql中；用户登陆，判断用户是否注册过，如果注册了，进行密码验证，如果验证超过3次，则30s后重试，验证次数和过期时间都会存在redis中。
  - 房屋模块，获取房屋列表，根据输入的页号、日期等条件筛选数据，并且过滤掉已经被下单的数据，对筛选出的结果排序，排序方式支持：发布时间降序（默认）、房屋价格升序和降序、被预定过的数量降序；房屋详细信息，除了重数据库中获取房子的基本信息外，如果房子之前被预定过，还需要查询数据库，获得订单的评论信息一起显示；发布房源，对前端提交的数据依次进行校验，因为一个房子可能对应多个设施，再保存房子信息的同时，房子设备对应关系也应该同时保存；房屋图片保存，房主上传的图片，保存到服务器上（七牛云），返回的image_url存入数据库。
  - 订单模块，生成订单，检查订单中的房子是否存在、预定日期是否有效，并且保证当前房子的预定日期内，没有人入住，同时房主不能预定自己发布的房源，避免刷单；订单列表，房主可以获取自己发布的房子，被预定的订单列表，也可以获得预定的其他房子列表；订单确认，租户提交订单后，房主可以看到请求的订单，只有在房主确认出租后，用户才可以支付；订单评论，当订单处于COMPLETE状态时，租户可以进行评论；订单详情，显示订单与房主租户的对应关系及评论信息。
  - 支付模块，检查订单是否存在，并且处于WAIT_PAYMENT状态，支付的用户是当前登陆的用户，验证通过后，使用支付宝sdk工具，跳转到支付界面。

  