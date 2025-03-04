# 基于 Ubuntu 22.04
FROM ubuntu:22.04

# 复制 run.sh 文件到容器中的 /app 目录
COPY run.sh /app/run.sh

# 设置工作目录为 /app
WORKDIR /app

# 赋予 run.sh 执行权限
RUN chmod +x run.sh

# 设置容器启动时运行的命令
CMD ["bash", "run.sh"]

