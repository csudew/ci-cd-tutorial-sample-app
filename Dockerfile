FROM python:3.11-slim

WORKDIR /sample-app

COPY . /sample-app/

RUN pip install --no-cache-dir -r requirements.txt -r requirements-server.txt

ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"
ENV FLASK_APP=bootstrap.py

EXPOSE 8000/tcp

CMD ["sh", "-c", "flask db upgrade && gunicorn app:app -b 0.0.0.0:8000"]
