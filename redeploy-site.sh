#!/bin/bash
command tmux kill-server
PID=$(netstat -nlp | grep 0.0.0.0:5000 | awk '{print $NF}' | awk 'BEGIN { FS="/" } {print $1}')
if [[ $PID =~ ^[0-9]{0,}$ ]];
then
        command kill $PID
fi
command cd flask-blog-personal
command git fetch && git reset origin/main --hard
poetry install
command tmux new-session -d -s siteDeploy
command tmux send-keys -t siteDeploy.0 'cd flask-blog-personal; export DATOCMS_READONLY_TOKEN=9fdf53b2f8549a8c2ff31311d5d7d1 FLASKNV=production FLASK_DEBUG=off; poetry run flask run --host=0.0.0.0' C-m
