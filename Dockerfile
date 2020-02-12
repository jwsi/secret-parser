FROM alpine
RUN apk install python3
COPY main.py /main.py
ENTRYPOINT ["python3", "/main.py"]
