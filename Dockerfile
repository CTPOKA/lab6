FROM centos
COPY lab5.py .
RUN yum install epel-release -y
RUN yum install python36 -y
CMD python3 lab5.py
