FROM registry.redhat.io/ubi9/python-39@sha256:40a58935b9c22664927b22bf256f53a3d744ddb7316f3af18061099e199526ee

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api_request:app"]
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "api_scheduler:app"]