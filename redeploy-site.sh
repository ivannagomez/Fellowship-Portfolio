#!/bin/bash

tmux kill-server

cd ~/project-22-sum-21-regina-ivanna-gomez
git fetch
git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -ds flask-portfolio 'flask run --host=0.0.0.0;'
