FROM ubuntu:20.04
USER root
EXPOSE 5000/tcp
RUN apt-get update
RUN apt install wget curl -y
RUN apt remove libmariadb3 libmariadb-dev && apt autoremove
RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
RUN chmod +x ./mariadb_repo_setup
RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
RUN apt-get update
RUN apt install libmariadb3 libmariadb-dev -y
RUN apt-get install python3-pip  -y
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt --no-cache-dir
CMD python3 app.py