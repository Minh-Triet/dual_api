# Sử dụng base image Python
FROM python:3.8

# Thiết lập đường dẫn làm việc
WORKDIR /app

# Copy các file cần thiết vào container
COPY requirements.txt .
COPY scheduler.py .

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Chạy Flask scheduler
CMD ["python", "scheduler.py"]