FROM prefecthq/prefect:2.16-python3.10
RUN apt-get update && apt-get install wget

WORKDIR /opt/prefect/dezoomcamp_final_project
ARG WDIR=/opt/prefect/dezoomcamp_final_project

RUN wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
RUN tar xzfv openjdk-11.0.2_linux-x64_bin.tar.gz

ENV JAVA_HOME "$WDIR/jdk-11.0.2"
ENV PATH "$PATH:$JAVA_HOME/bin"

RUN wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
RUN tar xzfv spark-3.3.2-bin-hadoop3.tgz

ENV SPARK_HOME "$WDIR/spark-3.3.2-bin-hadoop3"
ENV PATH "$PATH:$SPARK_HOME/bin"

ENV PYTHONPATH "$SPARK_HOME/python/:$PYTHONPATH"
ENV PYTHONPATH "$SPARK_HOME/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"
ENV PYTHONPATH "$WDIR:$PYTHONPATH"

RUN pip install -U pip
RUN pip install pipenv

COPY [ "Pipfile", "Pipfile.lock", "./" ]
RUN pipenv install --system --deploy


ADD src /opt/prefect/dezoomcamp_final_project/src
ADD config.ini /opt/prefect/dezoomcamp_final_project
ADD .dlt /opt/prefect/dezoomcamp_final_project/.dlt