# 使用 Ruby 官方镜像
FROM ruby:3.2-slim-bookworm

# 安装系统依赖（包括中文字体支持和图形处理）
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
	fontconfig \
    fonts-noto-cjk \
    graphviz \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*


# 刷新系统字体缓存
RUN fc-cache -f -v    

RUN apt-get update && apt-get install -y --no-install-recommends \
    ruby-full \
    graphviz \
    default-jre \
 && gem install --no-document asciidoctor asciidoctor-pdf asciidoctor-diagram \
 && rm -rf /var/lib/apt/lists/*


# 安装 Asciidoctor 核心工具链
RUN gem install \
    asciidoctor \
    asciidoctor-pdf \
    asciidoctor-diagram \
    rouge \
    prawn-table



# 安装用于数学公式渲染的二进制库
RUN apt-get update && apt-get install -y \
    libm17n-0 \
    libfontconfig1
    

# 设置工作目录
WORKDIR /workspace

# 安装字体管理工具
RUN apt-get update && apt-get install -y fontconfig

# 创建字体目录并拷贝
RUN mkdir -p /usr/share/fonts/truetype/custom
COPY ./fonts/*.ttf /usr/share/fonts/truetype/custom/

# 刷新系统字体缓存
RUN fc-cache -f -v