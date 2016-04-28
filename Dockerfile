FROM python:2.7

RUN apt-get update && \
    apt-get install -y --no-install-recommends\
    python-pip \
&& apt-get clean \
&& apt-get autoclean \
&& rm -rf /var/lib/apt/lists/*

ENV WD=/opt/prelurn
COPY . /opt/prelurn
WORKDIR /opt/prelurn

RUN pip install virtualenv
RUN virtualenv -p python2.7 venv

# Setting these environment variables are the same as running
# source /opt/learn/venv/bin/activate.
# ENV VIRTUAL_ENV /opt/prelurn/venv
# ENV PATH /opt/prelurn/venv/bin:$PATH
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install --upgrade .[test]
