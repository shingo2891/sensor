#!/bin/bash
#
# cron_sensor.sh
# cron実行用

cd ~/share/sensor
source .envs/venv/bin/activate
#~/sensor/xively_test.py
~/share/sensor/main.py
deactivate

# crontabへ追加
# crontab -e
# 1,11,21,31,41,51 * * * * /home/shingo/share/sensor/cron_sensor.sh



