#!/bin/bash

cd /home/uliw/user/python-scripts/PNTA

find . -name "*.ipynb" -exec rm {} \;

rsync --delete --recursive --copy-links --exclude-from=exclude_files.txt . ../PNTA-Notebooks/

