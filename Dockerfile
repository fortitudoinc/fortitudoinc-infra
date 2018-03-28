FROM ubuntu

RUN apt-get update && apt-get upgrade -y && apt-get install openssh-server -y
RUN mkdir -p /root/.ssh

COPY ssh-keys/id_rsa.pub /root/.ssh/authorized_keys

EXPOSE 8080
EXPOSE 443
EXPOSE 80
EXPOSE 22

ENTRYPOINT service ssh start && tail -f /var/log/dmesg

