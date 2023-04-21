# Select Image
FROM python:3.7.12-slim

# mode to code dir
WORKDIR /code

# copy the requirement.txt file
COPY ./requirements.txt /code/requirements.txt

# run the pip install command
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the app dir 
COPY ./app /code/app

# expose the port 
EXPOSE 5000

# run the service using uvicorn
CMD ["python","app/main.py"]
