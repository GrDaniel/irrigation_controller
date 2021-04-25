#! /bin/bash

source venv/bin/activate
rshell --buffer-size=30 -p /dev/ttyUSB0 -a rsync -m ../src/ /pyboard
