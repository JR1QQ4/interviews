# 常用的指令
cp /test1/file1 /test3/file2  # 如将/test1 目录下的 file1 复制到/test3 目录，并将文件名改为 file2
mv /test1/file1 /test3/file2  # 如将/test1 目录下的 file1 移动到/test3 目录，并将文件名改为 file2
mv * ..  # 当前目录所有文件移动到上一级目录
ps -ef|grep xxx  # 显示进程 pid
kill  # 使用 kill 命令来终结进程。先使用 ps 命令找到进程 id，使用 kill -9 命令，终止进程
tar -xvf file.tar  # 解压 tar 包
unzip file.zip  # 解压 zip
unrar e file.rar  # 解压 rar
free -m  # 查看服务器内存使用情况

ps -ef | grep java  # 查看所有 java 进程
ps -aux | grep java  # -aux 显示所有状态
kill -9 [PID]  # 杀掉某个服务的进程

cd /java/tomcat/bin
./startup.sh  # 启动 Tomcat 服务
./shutdown.sh  # 停止 Tomcat 服务命令

tail -f xx.out  # 查看日志
tail -1000 xx.out  # 查看最近 1000 行日志

netstat -anp | grep 端口号  # 查看某个端口是否被占用，LISTEN 表示已经被占用
netstat -nultp  #  LISTENING 并不表示端口被占用

find . -type f -size +100M  # 查找一个文件大小超过 5M 的文件
find / -name tnsnames.ora  # 如果知道一个文件名称，怎么查这个文件在 linux 下的哪个目录
locate tnsnames.ora  # 还可以用 locate 来查找
find / -name httpd.conf  # 在根目录下查找文件 httpd.conf，表示在整个硬盘查找
find /etc -name httpd.conf  # 在/etc 目录下文件 httpd.conf
find /etc -name 'srm'  # 使用通配符(0 或者任意多个)。表示在/etc 目录下查找文件名中含有字符串‘srm’ 的文件
find / -amin -10   # 查找在系统中最后 10 分钟访问的文件(access time)
find / -atime -2  # 查找在系统中最后 48 小时访问的文件
find / -empty   # 查找在系统中为空的文件或者文件夹
find / -group cat  # 查找在系统中属于 group 为 cat 的文件
find / -mmin -5  # 查找在系统中最后 5 分钟里修改过的文件(modify time)
find / -mtime -1  # 查找在系统中最后 24 小时里修改过的文件
find / -user fred  # 查找在系统中属于 fred 这个用户的文件
find / -size +10000c  # 查找出大于 10000000 字节的文件(c:字节， w:双字，k:KB， M:MB， G:GB)
find / -size -1000k  # 查找出小于 1000KB 的文件

# 测试环境搭建-tomcat
# 环境准备：Java 和 tomcat 的环境准备参考这篇 https://www.cnblogs.com/yoyoketang/p/10186513.html
rpm -qa | grep wget  # 打开 Xshell 连上服务器，先看 CentOS 系统有没自带 wget 这个工具
yum install wget
# 下载 jenkins
# 可以在本地下载之后，使用 Xftp 工具传到 tomcat 的 "/usr/share/tomcat/webapps"目录下
# 也可以直接使用 wget 工具下载到 linux 服务器上
mkdir /usr/share/tomcat/webapps/jenkins
cd /usr/share/tomcat/webapps/jenkins
wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war
# 切换源，然后重复上述步骤
cd /etc/yum.repos.d/
mv CentOS-Base.repo CentOS-Base.repo.back #建议备份或者改名
wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum makecache #生成缓存
jar -xvf jenkins.war  # 解压 war 包
# 启动 jenkins
# 浏览器输入： http://公网 ip:8080/jenkins 就能访问了（打不开的话重启 tomcat）
# 如果 Getting Started 页面遇到插件下载失败，打开 jenkins->系统管理->管理插件->高级
# 把： https://updates.jenkins-ci.org/update-center.json
# 换成： http://mirror.esuni.jp/jenkins/updates/update-center.json
# 或者 https 换成 http: http://updates.jenkins.io/update-center.json

# 文件上传与下载（rz，sz）
yum -y install lrzsz
mkdir /root/testfile
cd /root/testfile
# 上传文件
rz
# 下载文件
sz filename

# python环境搭建
mkdir /root/python36
cd /root/python36
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
tar -xvf Python-3.6.8.tgz
cd Python-3.6.8
./configure --prefix=/root/python36
make
make install
ln -s /root/python36/bin/python3.6 /usr/bin/python3
python3 -V
ln -s /root/python36/bin/pip3 /usr/bin/pip3
pip3 -V

# java环境搭建
rpm -qa | grep yum
rpm -qa | grep java
# 如果没有 java 环境，接着就去查找java-1.8.0的可以使用的安装包
yum list | grep java-1.8.0-openjdk
yum -y install java-1.8.0-openjdk*
java -version
javac
# 或者使用解压的方式
tar -xvf jdk-8u65-linux-x64.tar.gz
vim /etc/profile
export JAVA_HOME=/home/software/jdk1.8.0_65
export JRE_HOME=/home/software/jdk1.8.0_65/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
source /etc/profile
java -version





