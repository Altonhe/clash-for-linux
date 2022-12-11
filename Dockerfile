FROM python:3.10 as builder
COPY . /app
RUN pip install -r requirements.txt
RUN python build.py

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app /app
CMD ["bash", "start.sh"]