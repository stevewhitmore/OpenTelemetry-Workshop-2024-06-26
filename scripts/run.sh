#!/bin/bash

cd aspire
docker compose up -d

# export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
# opentelemetry-instrument \
#     --traces_exporter console \
#     --metrics_exporter console \
#     --logs_exporter console \
#     --service_name dice-server \
#     flask run -p 8080

cd ../scripts
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument --logs_exporter otlp flask run -p 8080 &


flask --app age.py run -p 5000 &