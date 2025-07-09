# Run Instructions

To run the training pipeline, follow these steps from main directory:

1- Create a directory for model artifact:
```
mkdir -p artifacts
```
2- Place the `train.csv` and `test.csv` files in the `training/data/` directory. These files are not included in the repository due to client confidentiality. If a different directory is used, update the `config.py` file accordingly.

3- Build the Docker image:
```
docker build -t training-pipeline training/.
```
4- Run the Docker container, mounting the artifacts directory to save output:
```
docker run --rm -v $(pwd)/artifacts:/app/output training-pipeline
```

5- The trained model will be saved in the `artifacts/` directory as `model.pkl`.