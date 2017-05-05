# Code Directory. 

**##Step 1: 3rd Party Library Installation**

The Adafruit library is responsible for the DHT_22 functioning properly.
Without installing this library you cannot use the DHT_22 sensor.

To begin, open your linux terminal and then do the following-
```
git clone https://github.com/N02775223/ELSpring2017
sudo apt-get install build-essential python-dev
cd ELSpring2017
cd Adafruit_Python_DHT
sudo python setup.py install
cd ..
```

**##Step 2: Installing Expect and Bash**

This project uses shell scripts to automate everything. You do not need to run these scripts for the program to work, but it's highly recommended.
```
sudo apt-get install expect
sudo apt-get install bash
chmod a+x Expect.exp
chmod +x Wyvern.sh
chmod +x Wyvern2.sh
```

**##Step 3: Setting Up Your Local Server and PHPMyAdmin**

This step is required for exporting your local MySQL database and inserting the data from your sensors.
```
sudo apt-get install mysql-server mysql-client php5-mysql
-There should be a prompt asking you to set a password for the "root" user and then enter 'mysql -u root -p'
-Type 'quit' in the command line to exit the MySQL database.
sudo apt-get install python-mysqldb
sudo apt-get install apache2 php5 libapache2-mod-php5
sudo apt-get install phpmyadmin
sudo nano /etc/apache2/apache2.conf
-Put this line at the bottom of the apache2.conf file 'Include /etc/phpmyadmin/apache.conf'
-Press CTRL X and Y to save your changes.
sudo /etc/init.d/apache2 restart
-Type 'ifconfig' in your terminal and grab your IP address from it.
-Put the IP address in your web browser and it should look like this http://192.170.1.150/
-Now put 'http://192.170.1.150/phpmyadmin' and you should be greeted by a new webpage saying "Welcome to phpMyAdmin"
Your local server MySQL server should officially be setup now.
```

