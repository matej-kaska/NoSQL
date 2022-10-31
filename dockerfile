FROM ubuntu:20.04
USER root
RUN apt-get update
RUN apt install wget curl -y
RUN apt remove libmariadb3 libmariadb-dev && apt autoremove
RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
RUN echo "733cf126b03f73050e242102592658913d10829a5bf056ab77e7f864b3f8de1f  mariadb_repo_setup" | sha256sum -c -
RUN chmod +x ./mariadb_repo_setup
RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
RUN apt-get update
RUN apt install libmariadb3 libmariadb-dev -y
RUN apt-get install python3-pip  -y
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /code
CMD python3 app.py