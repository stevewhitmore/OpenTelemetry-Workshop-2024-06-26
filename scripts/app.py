from flask import Flask, request
import logging
import json
import requests

# These are the necessary import declarations
from opentelemetry import trace
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Acquire a tracer
tracer = trace.get_tracer("person-parent.tracer")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def get_person():
    with tracer.start_as_current_span("person-parent-request") as person_span:
        firstname = request.args.get("firstname", default = None, type = str)
        surname = request.args.get("surname", default = None, type = str)
        person_span.set_attribute("person.value", f"{firstname} {surname}")
        age_request_result = requests.get('http://127.0.0.1:5000/')

        result = {
            "firstname": firstname,
            "surname": surname,
        }

        if (age_request_result.json() is not None):
            result["age"] = age_request_result.json()["age"]

        return json.dumps(result)
