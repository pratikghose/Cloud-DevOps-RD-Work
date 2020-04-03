# getting base image ubuntu
FROM ubuntu
#FROM scratch - to build a completly empty image and then add to it

MAINTAINER pratik pal <pratikghose1999@gmail.com>
RUN apt-get update
CMD ["echo","Hello World..! from my first docker image"]
#diff between run and cmd is run gets executed during the building of the image, whereas the commands in cmd are only executed when you make a container out of the image.