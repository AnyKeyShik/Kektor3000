FROM python:3.8
COPY . /Kektor3000
WORKDIR /Kektor3000
RUN pip3 install -r requirements.txt
ENV Kektor3000_HOME /Kektor3000
RUN mkdir /Kektor3000/logs
CMD python ./run.py