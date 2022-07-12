FROM quay.io/centos/centos:stream8

RUN dnf install -y python3.9

WORKDIR /Fellowship-Portfolio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

EXPOSE 5000
