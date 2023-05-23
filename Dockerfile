# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files to the working directory
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD [ "python", "app.py" ]
