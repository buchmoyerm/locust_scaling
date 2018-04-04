FROM python:3.5
ADD . /work
WORKDIR /work
RUN pip install -r requirements.txt
ENTRYPOINT ["locust", "--slave"]
