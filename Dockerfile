FROM python:3.8

USER root

COPY app /var/www/betting_software
COPY requirements.txt /tmp/requirements.txt

WORKDIR /tmp

RUN pip3 install -r requirements.txt

WORKDIR /var/www/betting_software

RUN chmod -R 777 /var/www

EXPOSE 8000 8000

CMD ['run.py']