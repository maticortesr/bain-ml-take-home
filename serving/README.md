# Run Instructions

1- Create a .env file in the `serving` directory for the API key:
```
BAIN_API_KEY=YOUR_API_KEY_HERE
```


2- Build the Docker image:
```
docker build -t api-server -f serving/Dockerfile .
```
3- Run the Docker container:
```
docker run --rm  -p 8080:8080 --env-file serving/.env api-server
```

4- Test the API with a sample request:
```bash

curl  -X POST \
  'http://0.0.0.0:8080/predict' \
  --header 'X-API-Key: YOUR_API_KEY_HERE' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "model_version": "1",
  "model_features": {"type" : "departamento","sector": "providencia","net_usable_area": 70.0,"net_area": 79.0,"n_rooms":2.0,"n_bathroom":2.0,"latitude":-33.44425,"longitude":-70.61317}
}'

```

5- Example response:
```json
{
"status":"success",
"model_version":"1",
"prediction_label":"price",
"prediction_value":7424
}
```
