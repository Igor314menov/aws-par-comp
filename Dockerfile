FROM  python:3.8.2-slim-buster

COPY main.py /main.py

ENTRYPOINT ["python3", "main.py"]
