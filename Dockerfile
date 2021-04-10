FROM centos
COPY lab6.py .
RUN yum install epel-release -y
RUN yum install python36 -y
CMD python3 lab6.py
