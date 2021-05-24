#! /bin/bash

# Active virtualenv
source venv/bin/activate

# Copy files
rshell --buffer-size=30 -p /dev/ttyUSB0 -a rsync -m ../src/ /pyboard

# List files
rshell -p /dev/ttyUSB0 ls -all /pyboard/

# Soft Reset
pyboard --device /dev/ttyUSB0 -c 'import sys; sys.exit()'
