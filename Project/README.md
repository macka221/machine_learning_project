# Instructions On Starting the Robot

## *Goal*

1. Run a toy vehicle autonomously using Jetson Nano GPU Card.
2. Train an object detection neural network on images of road signs
3. The robot should navigate autonomously using the model

## *Requirements*

- Ubuntu 18.04LTS or later (Jetbot)
- Cuda 10.2.89 (Jetbot)
- Cudnn 8.0.0.180 (Jetbot)
- Tensorrt 7.1.3.0 (Jetbot)
- GStreamer (recieving computer)
- PyTorch (Jetbot)
- Jetson-Inference Code (Jetbot)
- CVAT (work computer)

## *Resources*

(Information About JetPack)[https://developer.nvidia.com/embedded/jetpack-sdk-45-archive]

## Instructions

### **1. Setup**

Print out or create signs for turning right, u-turns, and turning left. Connect the Jetbot to a monitor, mouse and keyboard then connect it to Wifi. The username and password for the Jetbot is "jetbot". Next install Gstreamer on your recieving computer.

### **2. Initial Load**
```bash
$ sudo nmcli device wifi connect <SSID> password <PASSWORD>
```

The line above connects to a wifi connection from the Jetbot. This can also be done by using the wifi bar in the top right corner of the OS.

```bash
$ sudo systemctl set-default graphical.target
```

This command enables the GUI interface of the jetbot. Next verify the time settings in the machine aligns with current time zone. Finally run the following command to reboot the jetbot.

```bash
$ sudo reboot
```

### **3. [Optional] Disable sudo password prompt

Since we have to use sudo a lot to operate the jetbot, we can disable it using the following commands:

```bash
$ sudo -i

$sudo vim /etc/sudoers
```
Add the below line to the end of the file, then click the Esc key and enter :wq to save the file.
```vim
jetbot ALL=(ALL) NOPASSWORD:ALL
```

### **4. Check Storage**

```bash
free -m
```

The above line fixesa a bug with nvidia softwares partitioning size. If the memory does not match the size of the SD card, execute the following:

```bash
$ cd ~/jetcard
$ git pull
...
$ git checkout jetpack_4.5.1
...
$ ./scripts/jetson_install_nvresizefs_service.sh
...
$ cd ../
$ rm -rf jetcard
...
$ sudo reboot
```

If using Jetpack version 4.4.1 onwards there is a bootloader issue. To solve this use the following instructions:

```bash
$ sudo vim /usr/sbin/l4t_payload_updater_t210
```

Go to the function def _/skip_/check_/old_/ver(self) and bypass it by inserting return True after it.

### **5. Apt-Get**

After adding the line to the l4t_/payload_/updater_/t210 you can run the following to update and upgrade software.

```bash
$ sudo apt-get update && sudo apt update
...
$ sudo apt-get upgrade && sudo apt upgrade
...
```

### **6. Jetson Inferene Installation**

#### *Links*
- (jetson inference computer vision models)[https://github.com/dusty-nv/jetson-inference]
- (jetson markdown instructions)[https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md]

Execute the following commands:

```bash
$ sudo apt-get update
...
$ sudo apt-get install git cmake libpython3-dev python3-numpy
...
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
...
$ cd jetson-inference
$ cmake ../
...
$ make -j$(nproc)
...
$ sudo make install
...
$ sudo ldconfig
...
```
Test the object detection model

```bash
$ cd arrch64/bin
$ detectnet --flip-method=rotate-180
...
```
### **7. Installing Packages**

Install the packages needed for operating motors using the following.

```bash
$ sudo apt-get update && sudo apt-get upgrade
...
$ sudo apt-get install python3-pip
...
$ pip3 install traitlets
...
$ pip3 install packaging
...
$ pip3 install ipywidgets
...
$ sudo apt-get install libopenblas-base libopenmpi-dev libomp-dev python3-opencv
...
$ pip3 install Cythonhe search pattern
...
$ pip3 install numpy torch-1.8.0-cp36-cp36m-linux_aarch64.whl
...
$ pip3 install adafruit-circuitpython-motorkit
...
$ pip3 install Adafruit_motorHAT
...
$ pip3 install keyboard
...
$ sudo apt-get install python3-pip
...
$ wget https:/bootstrap.pypa.io/pip/3.6/get-pip.py
...
$ python3 get-pip.py
...
$ sudo pip3 uninstall Pillow && pip3 Pillow==8.0.1
...
$ pip3 install --upgrade setuptools
...
$ pip3 install keyboard inputs traitlets packaging ipywidgets Adafruit_MotorHAT
...
$ cd $HOME
...
$ git clone https://github.com/NVIDIA-AI-IOT/torch2trt
...
$ cd torch2trt
$ sudo python3 setup.py install
...
```

### **8. Example Code**

Copy the jetbod folder from the drive. **Note: src is where all the code will be located**

----
### <b><i><u>Steps 2-8 are if it becomes necessary to rebuild the jetbot</u></i></b>
----
### **9. Connecting to Jetbot**

In 


