# Linux Subsystem on Windows 10

To check if we run in linux subsystem



Follow this to set a password
* <https://askubuntu.com/questions/772050/reset-the-password-in-ubuntu-linux-bash-in-windows>


* do not install cloudmesh-gui on Linux subsystem as GUIs are not sported

psutil needs to be installed like this

* sudo apt-get install gcc python3.7-dev
* pip install psutil

```

sudo apt-get update
sudo apt install wget>>> platform.uname()

This will be useful for test for installing mongod

platform.uname()
uname_result(system='Linux', node='DESKTOP', release='4.4.0-18362-Microsoft', version='#1-Microsoft Mon Mar 18 12:02:00 PST 2019', machine='x86_64', processor='x86_64')
>>> platform.system()
'Linux'
>>> platform.version()
'#1-Microsoft Mon Mar 18 12:02:00 PST 2019'


sudo apt install emacs
sudo apt-get -y install libcurl4 openssl

# Set up Git

sudo apt install git
git config --global user.name "Gregor von Laszewski"
git config --global user.email laszewski@gmail.com
git config --global core.editor emacs
git config --list

# Setup Python

sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3.7-dev
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.7 get-pip.py
sudo apt install python3.7-venv
python3.7 -m venv ~/ENV3
rm get-pip.py
pip install pip -U


# Install cloudmesh

pip install cloudmesh-installer
cloudmesh-installer git clone cloud
cloudmesh-installer install cloud -e

cms help
# There is a bug in the mongo install script that installs openssl, its better to
# take it out and do the install outside

cms admin mongo install --nosudo
cd *cloud

# The script has a bug as the path does not mask spaces ( and )
  
emacs ~/.bashrc
source ~/.bashrc

# Test things

which mongod
 
ssh-keygen
cms init
cms key list
``` 


this needs to be added to the previous atthe right location

mkdir cm
add the lines 

```
source ~/ENV3/bin/activate
cd cm
```

to your bashrc file

now when you start a new ubuntu shell, you are all set and can work on the install


