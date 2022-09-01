FROM python:3.7.9
COPY .  /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE  8000
CMD ["uvicorn", "app:app"]