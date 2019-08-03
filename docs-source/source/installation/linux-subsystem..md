# Linus Subsystem on Windows 10

    6  sudo apt-get update
    7  sudo apt install emacs
    9  sudo apt install git
   10  git config --global user.name "Gregor von Laszewski"
   11  git config --global user.email laszewski@gmail.com
   12  git config --global core.editor emacs
   13  git config --list

  251  sudo apt update
  252  sudo apt install software-properties-common
  253  sudo add-apt-repository ppa:deadsnakes/ppa
  254  sudo apt install python3.7

  259  sudo apt install python3.7-dev
  262  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  264  sudo python3.7 get-pip.py
  269  sudo apt install python3.7-venv
  271  python3.7 -m venv ~/ENV3
  273  rm get-pip.py

  276  pip install pip -U
  277  pip install cloudmesh-installer
  278  cloudmesh-installer git clone cloud
  279  cloudmesh-installer install cloud -e
  280  cms help
  295  sudo apt-get -y install libcurl4 openssl
  301  sudo apt install wget
  302  cms admin mongo install --nosudo
  304  cd *cloud

  #the script has a bug as the path does not mask spaces ( and )
   
    
  310  emacs ~/.bashrc
  311  source ~/.bashrc
  314  which mongod
 
  318  ssh-keygen
  319  cms init
  320  cms key list
 
