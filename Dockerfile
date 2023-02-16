FROM python:3.10
RUN apt-get update
    #&& \
    #apt-get install -y locales && \
    #cat /etc/locale.gen | grep -i -e tr_tr -e en_us | grep -i -e utf-8 | sed -e 's/# //' > /etc/locale.datadot.gen && \
    #cp /etc/locale.datadot.gen /etc/locale.gen && \
    #dpkg-reconfigure --frontend=noninteractive locales && \
    #update-locale LANG=en_US.UTF-8

RUN apt-get install sqlite3
WORKDIR /code

# copy files
COPY ./requirements.txt /code/requirements.txt
COPY ./antispeedbump-1.0.1-py3-none-any.whl /code/antispeedbump-1.0.1-py3-none-any.whl
COPY ./ dest

# RUN
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install antispeedbump-1.0.1-py3-none-any.whl 

COPY ./src /code/src
CMD ["python", "./src/api.py"]
