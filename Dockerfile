FROM python:3.8

USER root

COPY ./app /opt/betting_software
COPY requirements.txt /tmp/requirements.txt

WORKDIR /tmp

RUN pip3 install -r requirements.txt

WORKDIR /opt/betting_software
RUN mkdir -p logs && \
    touch logs/log.txt

ENV PYTHONPATH $PYTHONPATH:/opt/betting_software
CMD ["python", "run.py"]
