#!/bin/bash
command cd flask-blog-personal
command git fetch && git reset origin/main --hard
poetry install
command docker compose -f docker-compose.prod.yml down
command docker compose -f docker-compose.prod.yml up -d --build
