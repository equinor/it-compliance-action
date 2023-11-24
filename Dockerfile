FROM python:3

RUN pip install --no-cache pyyaml PyGithub

COPY /src /src

ENTRYPOINT [ "python", "src/main.py" ]