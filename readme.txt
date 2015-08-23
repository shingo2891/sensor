
##############################
# hisotry
##############################
# 2015/01/17 v0.01
# 2015/08/06 v0.02

##############################
#シリアルポートの権限設定
##############################
sudo chmod 666 /dev/ttyACM0
ls -l /dev/ttyACM0


##############################
# インストール
##############################
https://personal.xively.com/dev/tutorials/pi/
$ sudo apt-get update
$ sudo apt-get upgrade

$ sudo apt-get install git
$ sudo apt-get install python-setuptools

$ sudo easy_install pip
$ sudo pip install virtualenv

$ mkdir sensor
$ cd sensor

$ virtualenv .envs/venv

$ source .envs/venv/bin/activate

$ pip install xively-python
$ pip install pyserial

$ pip install pyflakes
$ pip install pep8

xively_test.py
FEED_ID = "修正"
API_KEY = "修正"




