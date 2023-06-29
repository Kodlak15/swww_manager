import os
from typing import Dict, List

def create_binding(dir: str, used: List) -> str:
    """
    Finds a binding for dir that has not been used yet
    """
    binding = dir[0] 
    while binding in used:
        idx = len(binding)
        binding += dir[idx] 
    return binding

def gen_mappings(config: Dict) -> Dict:
    """
    Creates mappings based on subdirectories in ./images
    """
    subdirs = [d.path for d in os.scandir("./images") if d.is_dir()]
    for d in subdirs:
        d = d.split('/')[2]
        if config["mappings"] == None:
            config["mappings"] = dict()
            config["mappings"][d] = create_binding(d, [])
        elif d not in config["mappings"].keys():
            used = config["mappings"].values()
            config["mappings"][d] = create_binding(d, used)
    return config
