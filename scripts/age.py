from flask import Flask
import logging

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
tracer = trace.get_tracer("person-child.tracer")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def roll_dice():
    with tracer.start_span("person-child-request") as person_age_span:
        person_age_span.set_attribute("person_age.value", "99")
        return { "age": 99 }
