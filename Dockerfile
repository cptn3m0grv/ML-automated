FROM centos:7

RUN yum install python3 -y 
RUN yum install libXext -y
RUN yum install libXrender -y
RUN yum install libSM -y
RUN pip3 install -U pip
#RUN pip install keras 
RUN pip install numpy
#RUN pip install tensorflow
RUN pip install pillow
RUN pip install opencv-python
RUN pip install sklearn
RUN pip install pandas
CMD python3 /root/lr.py
