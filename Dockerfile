FROM python:3.11-alpine
WORKDIR /app

COPY ./requirements.txt /code/requirements.txt
ARG MONGO_URI
ENV MONGO_URI=${MONGO_URI}
RUN echo MONGO_URI
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

EXPOSE 5000 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
