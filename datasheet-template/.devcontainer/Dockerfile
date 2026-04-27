FROM ruby:3.2-slim-bookworm

ARG PLANTUML_VERSION=1.2024.8
ARG NOTO_CJK_REF=main

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    chromium \
    curl \
    default-jre \
    fontconfig \
    fonts-dejavu-core \
    fonts-noto-cjk \
    git \
    graphviz \
    libfontconfig1 \
    libjpeg-dev \
    libm17n-0 \
    nodejs \
    npm \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN gem install --no-document \
    asciidoctor \
    asciidoctor-diagram \
    asciidoctor-pdf \
    rouge \
    prawn-table

RUN npm install -g playwright-core wavedrom@3.5.0

COPY phantomjs-shim.cjs /usr/local/lib/phantomjs-shim.cjs

RUN chmod +x /usr/local/lib/phantomjs-shim.cjs \
    && ln -sf /usr/local/lib/phantomjs-shim.cjs /usr/local/bin/phantomjs \
    && ln -sf /usr/local/lib/phantomjs-shim.cjs /usr/local/bin/wavedrom-renderer

RUN mkdir -p /usr/local/share/plantuml \
    && curl -fsSL "https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-${PLANTUML_VERSION}.jar" \
      -o /usr/local/share/plantuml/plantuml.jar

RUN mkdir -p /usr/local/share/fonts/noto-cjk-sc \
    && curl -fsSL "https://raw.githubusercontent.com/notofonts/noto-cjk/${NOTO_CJK_REF}/Sans/Variable/TTF/NotoSansCJKsc-VF.ttf" \
      -o /usr/local/share/fonts/noto-cjk-sc/NotoSansCJKsc-VF.ttf \
    && curl -fsSL "https://raw.githubusercontent.com/notofonts/noto-cjk/${NOTO_CJK_REF}/Sans/Variable/TTF/Mono/NotoSansMonoCJKsc-VF.ttf" \
      -o /usr/local/share/fonts/noto-cjk-sc/NotoSansMonoCJKsc-VF.ttf

RUN fc-cache -f -v

ENV DIAGRAM_PLANTUML_CLASSPATH=/usr/local/share/plantuml/plantuml.jar
ENV CHROMIUM_EXECUTABLE=/usr/bin/chromium
ENV NODE_PATH=/usr/local/lib/node_modules
ENV PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
ENV PHANTOMJS_EXECUTABLE=/usr/local/bin/phantomjs

WORKDIR /workspace
