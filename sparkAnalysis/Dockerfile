FROM datamechanics/spark:3.2.1-hadoop-3.3.1-java-11-scala-2.12-python-3.8-dm18

USER root

WORKDIR /opt/spark

RUN pip install --upgrade pip

COPY  requirements.txt .
RUN pip3 install -r requirements.txt
# RUN pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1
ENV PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1"

CMD jupyter-lab --allow-root --no-browser --ip=0.0.0.0