#!/bin/bash

cd /home/uliw/user/python-scripts/PNTA || exit

find . -name "*.ipynb" -exec rm {} \;

rsync --delete --recursive --copy-links --exclude-from=exclude_files.txt . ../PNTA-Notebooks/

