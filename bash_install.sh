#Instalation process for tradingStation on ubuntu 14.04
sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7 #must be python 2.9+
sudo apt-get update
sudo apt-get upgrade 									#python 2.9+
sudo pip install numpy									#numpy
sudo apt-get install libatlas-base-dev gfortran
sudo pip install scipy									#scipy
sudo pip install pandas									#pandas
sudo apt-get install python-matplotlib 					#must be version 1.4+
sudo apt-get install libfreetype6-dev
sudo pip install --upgrade python-matplotlib 			#matplotlib
sudo pip install quandl									#quandl
#Not checked:
	#sudo pip install statsmodels
	#sudo pip install scikit-learn



#Instalation for ubuntu 16.06

if [python -V = Python 2.7.12] #arreglar esto

sudo apt-get install python-pip

if [pip --version =  8.1.1]


#Github
sudo apt-get install git
mkdir /qubit-signalboy
cd /qubit-signalbot
git clone https://github.com/Camilo100/qubit-signalbot
cd /qubit-signalbot

#Tkinter (¿sirve?)
sudo apt-get install python-tk

#Drive
sudo apt install gnome-control-center gnome-online-accounts

#Ir a settings => online accounts => 
#https://www.howtogeek.com/196635/an-official-google-drive-for-linux-is-here-sort-of-maybe-this-is-all-well-ever-get/
#user: info@qcap.com.ar
#pass: QuantumCM2017


#Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo gdebi google-chrome-stable_current_amd64.deb

#Pip instalations
pip install pandas
pip install pandas-datareader
pip install matplotlib
pip install quandl
pip install numpy
pip install python-telegram-bot
pip install scipy
pip install -U scikit-learn 
pip install sklearn-pandas #https://github.com/scikit-learn-contrib/sklearn-pandas
pip install -U statsmodels

#Sublime text 3
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer

#Atom
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt install atom
