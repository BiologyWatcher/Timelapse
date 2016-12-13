#!/bin/bash
tmux new -d -s timelapse1 'sudo python timelapse.py'
tmux detach -s timelapse1
