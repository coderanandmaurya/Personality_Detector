# Personality Detector

## Run the API

Install the dependencies and start the FastAPI server from the project directory:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

The trained classifier and vectorizer must be present in the `model/` directory.
The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Predict a personality

Send text to `POST /predict`:

```json
{
  "text": "I enjoy spending a quiet evening reading."
}
```

The response contains the predicted personality:

```json
{
  "personality": "introvert"
}
```

Use `GET /health` to check that the API is running.