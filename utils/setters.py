from typing import Dict
import yaml
import subprocess

def set_config(config: Dict) -> None:
    with open("./config.yaml", "w") as stream:
        yaml.dump(config, stream)
    return

# Make transition customizable
def set_wallpaper(directory: str, image: str) -> None:
    subprocess.run([
        "/home/cody/bin/swww", 
        "img", 
        "--transition-type", 
        "outer", 
        "--transition-pos", 
        "0.75,0.9", 
        "--transition-step", 
        "90", 
        f"{directory}/{image}"
    ])
