import os
import yaml
import json 
import joblib
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError


from ChestCancerClassification import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file from the specified path and returns its content as a ConfigBox object.

    Parameters:
        path_to_yaml (Path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox object containing the content of the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs during the process.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded completed.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Empty yaml file.")
    except Exception as ex:
        raise ex
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created dir at path: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(json_path: Path) -> ConfigBox:
    with open(json_path) as f:
        content = json.load(f)
    logger.info(f"Json file: {json_path} loaded completed.")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved as binary in path: {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(filename=path)
    logger.info(f"Loaded binary file {path} succesfully.")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decode_image(imgstring, filename):
    img_data = base64.b64decode(imgstring)
    with open(filename) as f:
        f.write(img_data)
        f.close()
        

def encod_image_base64(cropedImagePath):
    with open(cropedImagePath, "wb") as f:
        return base64.b64encode(f.read()) 

