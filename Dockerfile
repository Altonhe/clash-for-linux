FROM python:3.10 as builder
COPY . .
RUN pip install -r requirements.txt
RUN python build.py

FROM alpine:latest
COPY --from=builder . .
CMD ["bash", "start.sh"]