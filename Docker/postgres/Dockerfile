FROM postgres:13-alpine

RUN apk add --no-cache su-exec tini libc6-compat \
    && apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing gnu-libiconv \
    && apk --no-cache add gettext

ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8
