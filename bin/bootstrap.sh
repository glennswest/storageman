#!/bin/sh
pip install ../nvmetarget
export FLASK_APP=./storageman.py
flask --debug run -h 0.0.0.0

