FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install Ruby + tools + fonts for CJK PDF rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    ruby-full \
    build-essential \
    default-jre-headless \
    git \
    locales \
    fontconfig \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    graphviz \
    plantuml \
    entr \
    && rm -rf /var/lib/apt/lists/*

# Enable UTF-8 locale (important for Chinese)
RUN sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Install Asciidoctor toolchain
RUN gem install --no-document asciidoctor asciidoctor-pdf rouge asciidoctor-diagram asciidoctor-diagram-plantuml

# Upgrade PlantUML to include security module (required by asciidoctor-diagram)
RUN wget -q "https://github.com/plantuml/plantuml/releases/download/v1.2024.6/plantuml-1.2024.6.jar" -O /tmp/plantuml.jar && \
    mv /tmp/plantuml.jar /usr/share/plantuml/plantuml.jar

WORKDIR /workspaces
