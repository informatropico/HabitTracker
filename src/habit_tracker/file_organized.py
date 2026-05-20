import os
import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

data_path = "src/data"
resources_path = "src/resources"

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        logger.debug(f"Directory created or already exists: {path}")
    except Exception as e:
        logger.error(f"Error creating directory {path}: {e}")
        raise

def move_file(src, dst):
    try:
        os.rename(src, dst)
        logger.debug(f"Moved file from {src} to {dst}")
    except Exception as e:
        logger.error(f"Error moving file from {src} to {dst}: {e}")
        raise

def main():
    create_directory(data_path)
    elements = os.scandir(resources_path)
    for file in elements:
        if file.is_file() and file.name != ("acron.txt"):
            move_file(file.path, os.path.join(data_path, file.name))
        elif file.is_dir():
            move_file(file.path, os.path.join(data_path, file.name))

if __name__ == "__main__":
    main()