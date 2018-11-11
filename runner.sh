#!/bin/bash
. dev/bin/activate
python3 cubes.py < $1
deactivate
