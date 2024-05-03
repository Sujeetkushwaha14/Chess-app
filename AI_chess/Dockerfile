FROM python:3.10
EXPOSE 8000
WORKDIR /flask_app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","flask_app","0.0.0.0"]
