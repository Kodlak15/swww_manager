A simple wallpaper manager for wayland utilizing [swww](https://github.com/Horus645/swww).

Dependencies/prerequisites:

- A Linux environment using the Wayland display protocol
- The [swww](https://github.com/Horus645/swww) wallpaper daemon
- Python packages:
  - os
  - pyyaml
  - typing
  - argparse
  - subprocess

Instructions:

- Clone the repository: git clone https://github.com/Kodlak15/swww_manager
- Add the project path to your PATH variable
  - As an example, in your shells init script (.bashrc, .zshrc, etc) you may add the following: `export PATH="$HOME/bin/swww_manager/:$PATH"`
  - This obviously assumes you have a directory named bin in your users home folder
- Add images you want to use to the images directory
  - Images can be placed in categorized subfolders
  - Example structure:
    tree ./images
    ├── forest
    │   ├── forest1.jpg
    │   ├── forest2.jpg
    │   └── forest3.jpg
    ├── mountains
    │   ├── mountains1.jpg
    │   ├── mountains2.jpg
    │   └── mountains3.jpg
    ├── ocean
    │   ├── ocean1.jpg
    │   ├── ocean2.jpg
    │   └── ocean3.jpg
    .
    .

# TODO:

- Tidy up existing code
- Add support for animation customization
- Add multi-monitor support
- Consider creating a graphical user interface
- Improve documentation
