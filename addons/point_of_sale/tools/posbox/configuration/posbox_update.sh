#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo git --work-tree=/home/pi/izi/ --git-dir=/home/pi/izi/.git pull
sudo mount -o remount,ro /
(sleep 5 && sudo reboot) &
