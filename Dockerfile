FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN --mount=type=cache,target=/tmp/pip-cache,id=pip_cache \
    pip install --cache-dir /tmp/pip-cache -r requirements.txt \
 && pip freeze > requirements.freeze.txt \
 && python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt') ; nltk.download('punkt_tab')"

# Copy the rest of the application code
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8506

# Command to run the application
CMD ["streamlit", "run", "ezmapper.py", "--server.port=8506", "--server.address=0.0.0.0", "--logger.level=debug"]
