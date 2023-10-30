FROM python:3.9

COPY api_request /api_request
COPY api_scheduler /api_scheduler

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api_request:app"]
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "api_scheduler:app"]