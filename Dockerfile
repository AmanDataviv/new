FROM  python:3.12.0-alpine
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
EXPOSE 8000
RUN pip install -r requirements.txt
RUN pip install uvicorn
CMD ["uvicorn", "main:app","--host","0.0.0.0", "--port", "8000", "--reload"]