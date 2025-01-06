#!/bin/bash
# copy notebook files from the PNTA folder to the
# PNTA-Notebook folder, so that they can be synced
# to github. Next update the Quiz directory

eval "$(ssh-agent)"
ssh-add /home/uliw/.ssh/id_rsa

cd /home/uliw/user/python-scripts/PNTA || exit
rsync --delete --recursive --copy-links --exclude-from=exclude_files.txt . ../PNTA-Notebooks/

mp1=/home/uliw/user/python-scripts/PNTA-Notebooks
mp2=/home/uliw/user/toronto/teaching/ESS245/Quizzes/
myArray=($mp1 $mp2)

for d in "${myArray[@]}"; do
    echo git -C "$d" add --all
    git -C "$d" add --all
    echo git -C "$d" commit -m "auto deploy"
    git -C "$d"  commit -m "auto deploy"
    echo git -C "$d" push -u origin main
    git -C "$d" push -u origin main
done
