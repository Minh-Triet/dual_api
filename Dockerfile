FROM registry.redhat.io/ubi9/python-39@sha256:40a58935b9c22664927b22bf256f53a3d744ddb7316f3af18061099e199526ee

COPY api_request /api_request
COPY api_scheduler /api_scheduler

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api_request:app"]
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "api_scheduler:app"]