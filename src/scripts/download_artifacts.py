import os
import boto3
from settings import Settings


def download_artifacts(settings: Settings):
    s3 = boto3.client("s3")
    artifacts = ["inference.py", "sentiment_tokenizer.joblib", "sentiment_model.joblib"]

    artifacts_dir = os.path.join(os.getcwd(), "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    for artifact in artifacts:
        s3.download_file(
            Bucket=settings.bucket_name,
            Key=artifact,
            Filename=os.path.join(artifacts_dir, artifact),
        )
