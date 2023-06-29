#!/usr/bin/python

import os
from utils.getters import get_config, get_parser, get_images, get_num_images, get_directories
from utils.setters import set_config, set_wallpaper
from utils.mappings import gen_mappings

if __name__ == "__main__":
    # Get the configuration
    try:
        config = get_config()
    except:
        config = {
            "current": {"directory": "./images/", "index": -1},
            "mappings": {"./images/", None}
        }

    # Update the mappings
    gen_mappings(config)

    # Get the program arguments
    parser = get_parser()
    args = parser.parse_args()

    # Get the path to the specified directory
    # If no directory specified, fallback to ./images
    if args.directory != None:
        directory = os.path.join("./images", args.directory)
    else:
        directory = "./images"

    # Get the names of all image directories
    # Assert that the specified directory is a valid one
    directories = get_directories()
    assert directory in directories, "Invalid directory!" 

    # If the specified directory is the same as the current one,
    # go to the next image in that directory, otherwise switch to
    # the new directory and set the index equal to 0
    if directory == config["current"]["directory"]:
        n = get_num_images(directory)
        assert n > 0, f"No images found in directory: {directory}"
        config["current"]["index"] = (config["current"]["index"] + 1) % n
    else:
        config["current"]["directory"] = directory 
        config["current"]["index"] = 0 

    # Set the updated configuration
    set_config(config)

    # Set the new wallpaper
    index = config["current"]["index"]
    images = get_images(directory)
    set_wallpaper(directory, images[index])
