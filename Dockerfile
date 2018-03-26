FROM ubuntu

RUN apt-get update && apt-get upgrade -y && apt-get install openssh-server -y

EXPOSE 8080
EXPOSE 443
EXPOSE 80
EXPOSE 22

ENTRYPOINT tail -f /var/log/dmesg

