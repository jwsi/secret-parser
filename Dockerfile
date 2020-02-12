FROM alpine
RUN apk add python3
COPY main.py /main.py
ENTRYPOINT ["python3", "/main.py"]
