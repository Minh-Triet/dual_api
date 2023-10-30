FROM registry.redhat.io/ubi9/python-39@sha256:40a58935b9c22664927b22bf256f53a3d744ddb7316f3af18061099e199526ee
EXPOSE 5000
COPY . /app
WORKDIR /app
USER 0
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org
ENV FLASK_APP /app/app.py

CMD ["/bin/bash", "docker.sh"]

