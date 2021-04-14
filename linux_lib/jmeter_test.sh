# Linux环境搭建
yum -y install java-1.8.0-openjdk*
yum -y install unzip
mkdir jmeter
cd jmeter
unzip apache-jmeter-5.1.1.zip

# 环境变量
# 解压完成后，接下来vi编辑/etc/profile文件，设置环境变量,在文件底部编辑
export PATH=/root/jmeter/apache-jmeter-5.1.1/bin/:$PATH
source /etc/profile
jmeter -v

# Linux上执行脚本
# 脚本文件（Test_Plan.jmx）导入linux服务器上
# -n 表示以no gui方式运行测试计划
# -t 表示测试计划，后面跟测试计划名称, 有空格的话用\空格表示
# -l表示测试结果，后面跟测试结果文件名称，后缀是.jtl文件
jmeter -n -t Test_Plan.jmx -l testplan.jtl
# 查看测试报告，testplan.jtl用jmeter打开

# 提取token
# 请求上添加后置处理器 -> JSON提取器
# 参数说明：
# Names of create variables 参数名称 token
# JSON Path expressions 提取表达式 $.token
# Match No.(0 for Random) 匹配规则，-1所有，0随机，1第一个 0
# Compute concatenation va 如果有匹配到多个值，选择此项，会将全部值保存到_ALL，并使用逗号分割每个值，需要Match No为-1
# Default Values没提取到就给默认值
# 之后再HTTP信息头管理器添加token，Authorization - Token ${token}

# 参数提取
# 正则表达式提取器
# 参数说明：
# 要检查的响应字段：样本数据源，默认选主体
# 引用名称：其他地方引用时的变量名称（re_token），自定义设置，引用方法：$.(引用名称)
# 正则表达式：数据提取器，（）括号里为你要获取的值，如“token”；“(.*?)”
# 模板：$$对应正则表达式提取器类型，-1全部，0随机，1第一个2第二个，若只有一个正则一般就写$1$
# 匹配数字：正则表达式匹配数据的所有结果可以看作一个数组，匹配数字即可看作时数组的第几个元素，-1表示全部，0随机，1第一个2第二个，若只要获取到匹配的第一个值，则写1
# 缺省值：匹配失败时的默认值，可以随便写各，不写也可以，或者勾选失败时候使用空值
# Xpath提取器

# Cookie管理器

# 断言

# CSV参数化
# 参数说明
# 文件名 导入你的txt文件绝对路径
# 文件编码 一般为utf-8
# 变量名 自己设置的变量，如果只有一个变量就只写一个，多个变量英文逗号隔开
# 忽略首行 第一行是title就设置True
# 分隔符 一般是英文逗号
# 是否运行带引号 一般不用改，默认False
# 遇到文件结束时循环 它会循环从txt文件取值，如果全部取完了想继续就是True
# 线程共享模式 默认所有的线程就行






















