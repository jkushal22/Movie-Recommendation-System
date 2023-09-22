FROM ubuntu:20.04
COPY . /usr/app/
WORKDIR /usr/app/
RUN apt update && apt install python3 python3-pip -y\
    && pip3 install -r requirements.txt && pip3 install lxml
EXPOSE 8501
CMD streamlit run movies.py
