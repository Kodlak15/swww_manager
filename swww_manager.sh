#!/bin/bash

cd $HOME/Documents/projects/swww_manager/

case $1 in 
    -s|--space) python main.py -d space;;
    -f|--forest) python main.py -d forest;;
    -o|--ocean) python main.py -d ocean;;
    -m|--mountains) python main.py -d mountains;;
    *) python main.py;;
esac
