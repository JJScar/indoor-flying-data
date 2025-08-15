FROM python:3.12.11
WORKDIR /usr/local/app

# Installing dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . .

# Setup an app user so the container doesn't run as the root user
RUN useradd -m -s /bin/bash app
USER app

CMD ["python", "main.py"]