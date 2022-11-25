FROM python:3.9

LABEL maintainer="slobodian.mariia.work@gmail.com"

WORKDIR /root

COPY ./requirements.txt /root/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /root/requirements.txt
 
COPY ./app /root/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]