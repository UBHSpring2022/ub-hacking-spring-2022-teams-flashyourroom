# Raspberry Pi

Once the Pi is flashed, (or using an existing Pi) make sure python is setup right

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
```

and then

```bash
sudo pip3 install --upgrade setuptools
```

To install Blinka (Enables easy hardware usage on Pi)

```bash
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```


