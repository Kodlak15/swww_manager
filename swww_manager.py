#!/usr/bin/python

import os
from utils.getters import get_config, get_parser, get_images, get_num_images, get_directories
from utils.setters import set_config, set_wallpaper

if __name__ == "__main__":
    # Set working directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    # Get the configuration
    try:
        config = get_config()
    except:
        # config = {"directory": "./images/", "index": -1}
        config = {"directory": "./images/", "index": -1, "img": ""}

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
    if directory == config["directory"]:
        n = get_num_images(directory)
        assert n > 0, f"No images found in directory: {directory}"
        ### TODO (this is jank)
        if args.previous == []:
            index = (config["index"] - 1) % n
        else:
            index = (config["index"] + 1) % n
        ###
        config["index"] = index
        config["img"] = os.listdir(directory)[index]
    else:
        config["directory"] = directory 
        config["index"] = 0 
        config["img"] = os.listdir(directory)[0]

    # Set the updated configuration
    set_config(config)

    # Set the new wallpaper
    index = config["index"]
    images = get_images(directory)
    set_wallpaper(directory, images[index])
