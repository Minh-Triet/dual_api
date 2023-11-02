# Sử dụng base image Python
FROM  registry.redhat.io/ubi9/python-39@sha256:40a58935b9c22664927b22bf256f53a3d744ddb7316f3af18061099e199526ee
#FROM python:3.8
# Thiết lập đường dẫn làm việc
WORKDIR /app

# Copy các file cần thiết vào container
COPY . /app

# Cài đặt các dependencies
RUN /opt/app-root/bin/python3.9 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Chạy Flask API
ENV PORT=5000
ENV WORKERS=4

# Chạy ứng dụng bằng Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS app:app