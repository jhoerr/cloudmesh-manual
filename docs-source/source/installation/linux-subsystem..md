# Linus Subsystem on Windows 10

```

sudo apt-get update
sudo apt install wget
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
