#!/bin/bash
command cd flask-blog-personal
command git fetch && git reset origin/main --hard
poetry install
command systemctl daemon-reload
command systemctl restart myportfolio
