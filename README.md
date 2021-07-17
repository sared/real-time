# Real-time Subway Countdown Display

## Usage

This repository allows you to run a countdown clock display for the NYC Subway from the comfort of your own apartment, home or office. You can configure it to display the times for the exact train(s)/station(s) you desire. It runs via RGB LED panels, the Raspberry Pi 2, @hzeller's great [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix), and the MTA's real time API. Currently, the MTA disseminates real-time data for all lines and stops in the NYC subway system. For further information about the MTA's real time API please see their [developer site](http://web.mta.info/developers/).  For avoidance of doubt, this repository is in no way connected, endorsed, or licensed by the Metropolitan Transportation Authority ("MTA"). 

**Please note that these panels do not have built-in PWM control and therefore should be run by a real-time processor. This repository utilizes the Raspberry Pi which is not a real-time processor. With that said, there should be limited issues utilizing the Pi to drive two RGB LED matrix panels. The performance issues should be limited to slight artifacts in the image including some "static" which can be seen below. You may be interested in exploring the use of level-shifters, real-time Linux kernels, or a [real-time HAT](http://www.adafruit.com/products/2345), but these are currently untested.**

You can see a demo of the completed display on [YouTube](https://www.youtube.com/watch?v=BXbsdpKbUQQ)
[![Demo Video](https://img.youtube.com/vi/BXbsdpKbUQQ/0.jpg)](https://www.youtube.com/watch?v=BXbsdpKbUQQ)

## Requirements

### Hardware

While the cheapest option to source the hardware necessary for the project is likely Alibaba.com, it generally requires a lot of lead time. To get up and running quickly, I recommend [Adafruit](https://www.adafruit.com/). I have provided links to the exact products I purchased from Adafruit.

* [Raspberry Pi 2 - Model B](https://www.adafruit.com/products/2358)
* [Mini USB WiFi Module](https://www.adafruit.com/products/814)
* [8GB SD CARD (Optionally Preinstalled with Stretch Lite)](https://www.adafruit.com/product/2820)
* [5V 2A Power Supply w/ MicroUSB Cable](https://www.adafruit.com/products/1995)
* [2 16x32 RGB LED Matrix Panels](https://www.adafruit.com/products/420)
* [Female DC Power Adapter - 2.1mm Jack to Screw Terminal Block](https://www.adafruit.com/products/368)
* [5V 4A Power Supply](https://www.adafruit.com/products/1466)
* Solder/Insulated Wire (if you own a soldering iron) OR [Premium Female/Female Jumper Wires](https://www.adafruit.com/products/266)
* USB or wireless mouse/keyboard, HDMI cable, and display (all for initial Raspberry Pi setup)
* Mounting hardware
* Wire Stripper/Cutter

A 4GB SD Card can be used but will not be able to hold the full Raspbian install. You can instead use Raspbian Lite if using a small SD card but note that you will have to set up the GUI yourself. Everything for this project can absolutely be done from the command line though so a liteweight install is very doable.

### Software

In addition to a fresh install of [Raspbian](https://www.raspbian.org/), you will need to install these libraries:

* [PIL](http://www.pythonware.com/products/pil/)
* [python gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/code-samples?hl=en#python)
* @hzeller's [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix). Make sure to install this in the empty "rpi-rgb-led-matrix" directory in this repository.

## Installation

1. Get the Raspberry Pi up and running. 
   * If you didn't get an SD card with Raspbian pre-installed, download the [latest image](https://www.raspberrypi.org/downloads/) and follow the appropriate [installation guide](https://www.raspberrypi.org/documentation/installation/installing-images/). 
   * Connect the Raspberry Pi to a keyboard, mouse, and display. Insert the SD card. Insert the MicroUSB power adapter and wait for the system to boot. If the system does not boot, check this guide for [troubleshooting](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=28&t=58151). 
   * Login to the Pi if prompted using the default username "pi", and the default password "raspberry". 
   * Configure the Pi using the "raspi-config" configuration screen which should automatically launch. If not use `sudo raspi-config` to access the menu. Make sure to change the timezone to New York and to change the default password before connecting to the internet. I also recommend using SSH to connect to the Pi remotely going forward. For more detailed information on the menu, please use this [guide.](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
   ![Raspi-Config Menu](http://www.blogcdn.com/www.engadget.com/media/2012/08/expandrootfsopt1.png)
   * Update the packages
   ```
   sudo apt-get update
   sudo apt-get upgrade
   ```
   * Safely shutdown the system with `sudo shutdown -h now` and then unplug the power. 
   * Insert the USB WiFi adapter and boot up the system. Enter the GUI via `startx` and [configure the WiFi](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-raspbian).
2. With both the RGB LED matrices and Raspberry Pi disconnected from power, connect the two using the female to female wires OR solder. Either way, use following the [wiring diagram](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md), and make sure you are wiring to the input side of one of the RGB LED panels. Make sure that all ground connections on the RGB panels are connected to grounds on the Pi. To connect the two matrices together, simply use the IDC cable as pictured below.

![Wiring Example](http://i.imgur.com/lcoUGVK.jpg)

3. In order to connect the panels to a power source, I had to cut one end of the AMP style power cords above the plastic piece, strip the insulation off the last 1/2" of the wires, and connect them to screw terminal DC power adapter. Make sure you have the polarity of the wires correct. The red wires on my panels went to the positive (+) side of the screw terminals and the blue wires went to the negative (-) side. Make sure to handle the connection with care and I suggest wrapping it in electrical tape for safety and stability. 

4. With the matrices correctly wired to the Pi and connected to power, boot the Pi back on. Login using your new credentials, and navigate to the GUI via `startx`. Make sure you are connected to the internet, and open up the command prompt. Create a directory named "subwaydisplay" via `mkdir subwaydisplay` and navigate to the directory via `cd subwaydisplay`. Clone this repository into the folder via `git clone https://github.com/sared/real-time.git`. If you run into an error, make sure that you have git installed via `sudo apt-get install git`. Navigate to the "rpi-rgb-led-matrix" directory via `cd rpi-rgb-led-matrix` and clone @hzeller's [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix) via `git clone https://github.com/hzeller/rpi-rgb-led-matrix.git`. Run the `make` command to compile the files of this repository. 

5. Install [PIL](http://www.pythonware.com/products/pil/) and [python gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/code-samples?hl=en#python) via instructions from the provided links. 

6. Obtain a developer key from the [MTA](http://web.mta.info/developers/developer-data-terms.html) and update the "sampleconfig.py" file with this information. Rename this file to "config.py".


6. Navigate back to the "subwaydisplay" directory in the command prompt and run the "importdata.py" program with `python importdata.py`. You should see the RGB LED matrix panels come to life with the information for the uptown and downtown Wall Street 2/3 trains, and downtown 4/5 trains. You can adjust which trains are displayed by altering the config file with the appropriate station ids which can be found in the "StaticData" folder.


Optional Steps:

7. Enabling Remote Access to Your Display: I recommend enabling some form of remote access for your display so you don't need to attach a monitor to make changes or fix any connection issues which may arise. I recommend MobaXterm which I installed and linked to my Pi using the instructions found [here](https://www.raspberrypi.org/forums/viewtopic.php?t=1336910). The installation instructions can be found about halfway down that page. In brief, the instructions are as follows:

   * Make sure SSH is enabled on your Pi:
   ```
   sudo raspi-config
   ```
   and press Enter. Select option #5 (Interfacing Options) and press Enter. Then select option #P2 (SSH) and press Enter. You will be asked if you want to enable the SSH server. Select "Yes" and press enter. A popup will open saying the SSH server has been enabled. Select "Ok" and you will be returned to the main menu. Select Finish and press Enter to exit raspi-config.
   
   * Obtain Your Pi's IP Address
   ```
   hostname -I
   ```
   Note down the IP Address and then reboot the Pi by typing
   ```
   sudo reboot
   ```
   and then press enter.
   
   * Once your Pi has rebooted you will no longer need to physically access it. The rest of these instructions can be done remotely from your personal computer. The next instructions will split for those managing the display from a Windows computer and those using MacOS.
   
   
   *Windows*
   
    You will need to install an SSH client with X11 forwarding on your computer to remotely manage your Raspberry Pi. I recommend [MobaXterm](https://mobaxterm.mobatek.net/) as an excellent free client.
    * Once you have installed MobaXterm you can connect to your Raspberry Pi:
    ![Open MobaXterm](https://i.imgur.com/x0v9JjG.png)
    
    * Create a session by clicking on the "Session" icon on the toolbar.
    ![Create a Seesion](https://i.imgur.com/XTGn0HK.png)
    
    * Enter the IP address of the Raspberry Pi as well as the Raspberry Pi username. Make sure that X11 Forwarding is enabled by click on the Advanced SSH Settings tab. When ready, click OK. You will be asked to enter the password.
    ![Entering Session](https://i.imgur.com/HsRfOVJ.png)
    
    * Once logged in navigate to the python script for the Subway Display to remotely manage your new display!
    ```
    cd MTAdisplay
    cd real-time
    python importdata.py
    ```
    ![Launching Real-Time Display](https://i.imgur.com/VDO89y7.png)
    
    
   *MacOS*
   
    You will need to install an SSH client with X11 Forwarding capabilities on the computer you wish to run the Raspberry Pi applications on. In order for the applications to appear on the computer, you also need to install Xorg Server on the computer as well. On macOS, you will need to install XQuartz since no application comes with Xorg Server integrated. Once XQuartz has been installed, you can use Terminal to connect to your Raspberry Pi. To start an SSH session with X11 forwarding, type in:
     ```
     ssh -Y username@raspberrypiaddress
     ```
     where "username" is your Raspberry Pi username and "raspberrypiadrress" is your Raspberry Pi's IP address. Then press Enter. You may be asked if you are sure if you want to connect to the host. Type in "yes". Enter the Raspberry Pi password when asked.
     
     ![MacOS1](https://i.imgur.com/lpvrBmg.png)
     
     Once you are logged in, you are ready to launch Raspberry Pi applications remotely! To launch Subway display remotely, type in:
     ```
    cd MTAdisplay
    cd real-time
    python importdata.py
    ```
    
8. Keeping the Display Running When Remote Management Is Closed
   * One of the issues with remotely managing the Raspberry Pi is that when the connection is disconnected by default the Pi interprets the action as logging out and will stop all running programs including the Subway Display. The solution is to use tmux to create parallel sessions.
   * First install tmux:
   ```
   sudo apt-get install tmux
   ```
   * Then start tmux by typing tmux into the shell
   ```
   tmux
   ```
   * Then start the Subway Display process from inside the tmux session
   ```
   cd MTAdisplay
   cd real-time
   python importdata.py
   ```
   * Then detach the running tmux session with the Subway Display process running in it by typing Ctrl+B and then d
   
   * If you would like to check back on the running process you can access the tmux session by typing into the shell:
   ```
   tmux attach
   ```
   
   * If you would like a list of all running tmux sessions use
   ```
   tmux list-sessions
   ```

9. Launching Display on Boot
   * Ideally once everything is working you would want the Raspberry Pi to reboot and run the display without the hassle of SSHing in and starting the MTA display script yourself.
   
   * First create a launcher in the real-time directory
   ```
   cd
   cd MTAdisplay/real-time
   nano launcher.sh
   ```
   * Now editing the launcer in nano you will want to write the following script:
   ```
   #!/bin/sh
   # launcher.sh
   # navigate to home directory, then to this directory, then execute python script, then back home
   
   cd /
   cd home/pi/MTAdisplay/real-time
   sudo -H -u pi python importdata.py
   cd /
   ```
   * Ctrl-X and save the launcher
   
   
   * Now make this new launcher script an executable
   ```
   chmod 755 launcher.sh
   ```
   
   * Give it a test by running the launcher
   
   ```
   sh.launcher.sh
   ```
   
   * The display should be showing the train times correctly. Break the operation with Ctrl-c before proceeding.
   
   
   * Now we add a logs directory to the home directory to keep track of any errors. Navigate back to the home directory with
   ```
   cd
   ```
   
   * And then create the logs directory
   
   ```
   mkdir logs
   ```
   
   
   * We are going to make the display script trigger at startup using crontab, a background process which lets you execute scripts at specific times. It is confusing but we won't need to do much with it to get it to work!
   * In the home directory enter:
   
   ```
   sudo crontab -e
   ```
   
   * This will bring up crontab. You may be prompted to select the editor you would like to use. Choose nano, which in my case was helpfully marked as the "easiest" option in the terminal.
   
   * Once in crontab there will be a bunch of commented lines roughly introducing the syntax of the system. Below that enter the following line:
   
   ```
   @reboot sh /home/pi/MTAdisplay/real-time/launcher.sh >/home/pi/logs/cronlog 2>&1
   ```
   
   * This will execute the launcher at startup and record any errors in the logs directory we made earlier. Now see if it works!
   
   ```
   sudo reboot
   ```
   
   
   * If there are any issues check the log file:
   ```
   cd logs
   cat cronlog
   ```
   
   
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License

The MIT License (MIT)

Copyright (c) 2018 Stephen Redden

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
