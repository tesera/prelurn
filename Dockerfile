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

RUN . venv/bin/activate
RUN pip install --upgrade pip

# install dependencies so that they are cached
RUN pip install pandas==0.18.0 pytest==2.9.1 click==6.6 boto==2.40.0
RUN pip install .[test]
