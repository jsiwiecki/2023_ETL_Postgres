# Use the official Python base image
FROM python:3.8.16

# Set the working directory
WORKDIR /app

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk wget procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

ENV SPARK_VERSION 3.3.2
ENV HADOOP_VERSION 3
RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

ENV SPARK_HOME /opt/spark
ENV PATH $SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

RUN wget -q https://jdbc.postgresql.org/download/postgresql-42.4.2.jar -O /opt/spark/jars/postgresql-42.4.2.jar

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY scripts/create_tables.py .
COPY scripts/ingest_data.py .
COPY scripts/schemas.py .
COPY data/ .

ENV POSTGRES_HOST="postgres"
ENV POSTGRES_PORT="5432"
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

CMD ["sh", "-c", "python3 create_tables.py && python3 ingest_data.py"]