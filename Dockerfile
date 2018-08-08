FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python zip unzip wget curl bzip2
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
RUN bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /opt/miniconda2
ENV PATH $PATH:/opt/miniconda2/bin
RUN yes | conda update conda
RUN pip install -r requirements.txt
#RUN source activate /opt/biobuilds-2016.11
CMD ["/bin/bash"]
