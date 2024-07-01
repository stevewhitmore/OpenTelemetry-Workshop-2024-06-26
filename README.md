# Open Telemetry Workshop 2024-06-26-Wed

Notes and demo project from the 2024 KCDC workshop.

See [Notes](./opentelemetry-workshop-2024-06-26.md).

There are two apis; one calls the other. Our Aspire docker container runs and shows the traces/spans we have set up in "app.py" (see `run.sh`). 

## Running the project:

### Environment setup

Follow OpenTelemetry's [Getting Started docs](https://opentelemetry.io/docs/languages/python/getting-started/) to get the environment set up.

### Running it

There are two bash script for easy spin up and tear down of this demo project:

```bash
$ ./scripts/run.sh
```

```bash
$ ./scripts/stop.sh
```

The second script is necessary because both Flask API instances run in the background.

## Sources

- [OpenTelemetry getting started docs](https://opentelemetry.io/docs/languages/python/getting-started/)
- [OpenTelemetry Flask instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html)
- [Another python implementation](https://github.com/honeycombio/observability-day-workshop/tree/main/services/backend-for-frontend-python)