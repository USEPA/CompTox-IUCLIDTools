# Use the official Python 3.8 image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8506

# Command to run the application
CMD ["streamlit", "run", "ezmapper.py", "--server.port=8506", "--server.address=0.0.0.0"]
