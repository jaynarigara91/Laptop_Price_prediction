FROM python:3.10.15
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 6000
CMD ["streamlit", "run", "app2.py", "--server.port=6000", "--server.address=0.0.0.0"]