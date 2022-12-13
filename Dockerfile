FROM python:3.10 as builder
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python build.py

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app /app
RUN apk add --no-cache bash
RUN apk add --no-cache curl
RUN apk add --no-cache grep
RUN chmod +x start.sh
CMD ["bash", "start.sh"]