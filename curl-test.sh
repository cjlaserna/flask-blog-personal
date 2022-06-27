#!/bin/bash
echo $(curl http://localhost:5000/api/timeline_post)
echo $(curl -X POST http://localhost:5000/api/timeline_post -d 'name=example_name&email=example@email.com&content=Testing content')
