from settings import settings
from src.scripts.download_artifacts import download_artifacts


def main():
    download_artifacts(settings)


if __name__ == "__main__":
    main()
