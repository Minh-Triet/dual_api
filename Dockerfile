FROM registry.redhat.io/ubi9/python-39@sha256:40a58935b9c22664927b22bf256f53a3d744ddb7316f3af18061099e199526ee

COPY . /app
WORKDIR /app
USER 0
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]