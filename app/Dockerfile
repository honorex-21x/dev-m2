#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#WORKDIR /app

#COPY . /app

#RUN pip install --no-cache-dir -r /app/requirements.txt

#EXPOSE 80

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

#test git


#FROM python:3.6
#WORKDIR /app
#COPY . .
#RUN pip install -r requirements.txt
#CMD python app.py

FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
