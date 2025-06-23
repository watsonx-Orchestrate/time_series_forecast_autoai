# time_series_forecast_autoai

https://application-e5.1wrbgjmhze46.us-south.codeengine.appdomain.cloud

```bash
curl -X POST "https://application-e5.1wrbgjmhze46.us-south.codeengine.appdomain.cloud/predict" \
  -H "Content-Type: application/json" \
  -u "test:test" \
  -d '{
    "forecast_window": 3
  }'
```

로컬에서 확인.

```bash
pip install fastapi uvicorn
```
```bash
uvicorn time_series_autoai:app --host 0.0.0.0 --port 8080 --reload

```
```bash
curl -X POST "http://127.0.0.1:8080/predict" \
  -H "Content-Type: application/json" \
  -u "test:test" \
  -d '{
    "forecast_window": 3
  }'

```
