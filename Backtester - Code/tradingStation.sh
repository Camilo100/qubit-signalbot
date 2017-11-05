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


