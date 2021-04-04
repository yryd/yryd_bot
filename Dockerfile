# 基于镜像基础
FROM python:3.7
MAINTAINER yryd<youranyaodao@outlook.com>

# 设置代码文件夹工作目录 /app
ENV MYPATH /usr/local
WORKDIR $MYPATH
# 复制当前目录代码文件到容器中 /app
ADD . $MYPATH/yryd_run
# 安装所需的包与依赖
RUN pip install -r ./yryd_run/requirements.txt

EXPOSE 80
EXPOSE 8080
CMD /bin/bash
