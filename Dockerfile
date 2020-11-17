# Python base image.
FROM python:3.7

WORKDIR /my-project

# Execute a pip install command using the list 'requirements.txt'
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Copy all files into the image working directory

COPY . .

ENV DB_URI=$(DB_URI}
ENV SECRET_KEY=${SECRET_KEY}
# State the listening port for the container.
EXPOSE 5000

# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"]
