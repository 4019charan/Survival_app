FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 8051
WORKDIR /usr/app/
RUN pip install tornado==6.1
RUN pip install --upgrade pip
RUN pip install xgboost
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"]
