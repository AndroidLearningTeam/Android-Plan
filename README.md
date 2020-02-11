# Android-
当今海量的移动应用跟人们的生活、工作、学习、休闲、娱乐等方面密切相关，发挥着重要作用。多数APP在安装、更新时，都会向用户申请相关手机权限。多数终端用户缺乏鉴别APP所请求的权限是否合理的能力，并且APP安装使用过程中过度索要权限现象较为普遍，这就给用户数据安全、隐私信息泄露等留下了极大隐患。 本课题从Android权限模型、APP功能及行为出发，运用机器学习技术，对用户-APP-权限进行挖掘和关联分析，为恶意APP识别提供技术支持。

## Plan


1. 选择应用商店，爬虫获取APP的功能描述和权限申请内容。

2. 建立数据库，每个APP对应什么不同的权限，具有什么功能

3. 将权限分为两类，可给的，不可给的

![](https://github.com/AndroidLearningTeam/Android-Plan/blob/master/Res/1.PNG)
![](https://github.com/AndroidLearningTeam/Android-Plan/blob/master/Res/2.PNG)


### 

1. 爬取华为应用商店软件".apk"文件
https://github.com/AndroidLearningTeam/Android-Plan/blob/master/Crawler.py

2. 批处理".apk"文件, 提取应用xml描述文档
https://github.com/AndroidLearningTeam/Android-Plan/blob/master/get_xml.py
