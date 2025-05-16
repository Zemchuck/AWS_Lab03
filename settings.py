from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bucket_name: str = "my-test-lab6-aws-bucket"


settings = Settings()
