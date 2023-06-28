from utils.getters import *
from utils.setters import *

if __name__ == "__main__":
    # Get the configuration
    try:
        config = get_config()
    except:
        config = {"directory": "./images/", "index": -1}
        set_config(config)

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
        config["index"] = (config["index"] + 1) % n
    else:
        config["directory"] = directory 
        config["index"] = 0 

    # Set the updated configuration
    set_config(config)

    # Set the new wallpaper
    index = config["index"]
    images = get_images(directory)
    set_wallpaper(directory, images[index])
