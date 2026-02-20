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

# If your project provides custom fonts, add a `fonts/` folder to the project root.
# COPY ./fonts /usr/share/fonts/truetype/custom/
RUN fc-cache -f -v || true

WORKDIR /workspaces
