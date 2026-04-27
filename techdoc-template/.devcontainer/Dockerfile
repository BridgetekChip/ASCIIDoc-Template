FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install system dependencies, fonts, JRE, graphviz, plantuml
RUN apt-get update && apt-get install -y --no-install-recommends \
    ruby-full \
    build-essential \
    default-jre-headless \
    git \
    locales \
    fontconfig \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    fonts-mplus \
    graphviz \
    plantuml \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Enable UTF-8 locale
RUN sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Install Asciidoctor toolchain and common gems
RUN gem install --no-document asciidoctor asciidoctor-pdf asciidoctor-diagram rouge prawn-table

# Upgrade PlantUML to a known compatible release
RUN wget -q "https://github.com/plantuml/plantuml/releases/download/v1.2024.6/plantuml-1.2024.6.jar" -O /tmp/plantuml.jar \
 && mkdir -p /usr/share/plantuml \
 && mv /tmp/plantuml.jar /usr/share/plantuml/plantuml.jar

# Install region-specific Simplified Chinese fonts as standalone OTF files.
# This avoids ambiguous TTC collection resolution that can select the JP face.
RUN mkdir -p /usr/local/share/fonts/noto-cjk-sc \
 && wget -q "https://github.com/notofonts/noto-cjk/releases/download/Sans2.004/08_NotoSansCJKsc.zip" -O /tmp/NotoSansCJKsc.zip \
 && wget -q "https://github.com/notofonts/noto-cjk/releases/download/Sans2.004/13_NotoSansMonoCJKsc.zip" -O /tmp/NotoSansMonoCJKsc.zip \
 && unzip -oq /tmp/NotoSansCJKsc.zip -d /usr/local/share/fonts/noto-cjk-sc \
 && unzip -oq /tmp/NotoSansMonoCJKsc.zip -d /usr/local/share/fonts/noto-cjk-sc \
 && rm -f /tmp/NotoSansCJKsc.zip /tmp/NotoSansMonoCJKsc.zip

# If your project provides custom fonts, add a `fonts/` folder to the project root.
# COPY ./fonts /usr/share/fonts/truetype/custom/
RUN fc-cache -f -v || true

WORKDIR /workspaces
