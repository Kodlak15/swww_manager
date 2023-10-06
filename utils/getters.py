import os
from typing import Dict, List
import yaml
from argparse import ArgumentParser

def get_config() -> Dict:
    with open("./config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
            return dict()
    return config

def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory")
    ### TODO
    parser.add_argument("-p", "--previous", action="store", nargs="*")
    ###
    return parser

def get_directories() -> List:
    return ["./images"] + [f.path for f in os.scandir("./images/") if f.is_dir()]

def get_num_images(directory: str) -> int:
    return len([item for item in os.scandir(directory) if not item.is_dir()])

def get_images(directory: str) -> List:
    return sorted(os.listdir(directory))
