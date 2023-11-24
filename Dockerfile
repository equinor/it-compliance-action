FROM python:3

RUN pip install --no-cache pyyaml PyGithub

WORKDIR /usr/src

COPY src .

ENTRYPOINT [ "python", "/usr/src/main.py" ]