# Use the official Python image from the Docker Hub
FROM python:3.9

# Image Labels. Update values for each build
LABEL Name="Quest Forge"
LABEL Version=0.1
LABEL ReleaseDate="07.08.2024"
LABEL Description="Microservice with GenAI model generating quests for Skill Forge platform"
LABEL Maintainer="Aleksandar Karastoyanov <karastoqnov.alexadar@gmail.com>"
LABEL License="GNU GPL v3.0 license"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8001

# Run the Flask application
CMD ["python", "app.py"]