FROM almalinux:10

ENV LANG ja_JP.UTF-8
ENV TZ Asia/Tokyo

RUN groupadd -g 1000 pi
RUN useradd --uid 1000 --gid 1000 --shell /bin/bash -G pi pi

RUN ulimit -n 1024 && dnf update -y
RUN dnf install -y httpd python3 vim

COPY ./00-mpm.conf /etc/httpd/conf.modules.d/00-mpm.conf

RUN mv /etc/httpd/conf.d/welcome.conf /etc/httpd/conf.d/welcome.conf.bak

WORKDIR /home/pi

CMD ["/home/pi/entrypoint.sh"]
