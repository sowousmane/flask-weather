FROM python:3.9

# Set working directory
WORKDIR /app

ENV FLASK_APP=weather.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

EXPOSE 5000

# Run your application
CMD ["flask", "--app","weather.py","run"]
