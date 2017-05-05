# Code Directory.

**##Step 1: Setting Up Your Local Server and PHPMyAdmin**

This step is required for exporting your local MySQL database and inserting the data from your sensors.
To begin, open your linux terminal and then do the following-
```
sudo apt-get install mysql-server mysql-client php5-mysql
-There should be a prompt asking you to set a password for the "root" user and then enter 'mysql -u root -p'
-Type 'quit' in the command line to exit the MySQL database.
sudo apt-get install python-mysqldb
sudo apt-get install apache2 php5 libapache2-mod-php5
-Navigate to 'cd /var/www/html' and click on index.html to check if you've installed it correctly.
sudo apt-get install phpmyadmin
sudo nano /etc/apache2/apache2.conf
-Put this line at the bottom of the apache2.conf file 'Include /etc/phpmyadmin/apache.conf'
-Press CTRL X and Y to save your changes.
sudo /etc/init.d/apache2 restart

-If you make any changes to an apache file or if something goes wrong then type 'sudo service apache2 restart'
-Type 'ifconfig' in your terminal and grab your IP address from it.
-Put the IP address in your web browser and it should look like this http://192.170.1.150/
-Now put 'http://192.170.1.150/phpmyadmin'
```
You should be greeted by a new webpage saying "Welcome to phpMyAdmin" signalling that phpmyadmin has now been setup.

**##Step 2: Setting up your MySQL Database**
As a note, you may name the database or user as whatever you want.
```
mysql –u –p or mysql –u [ROOT] –p
CREATE DATABASE some_database;
SHOW DATABASES;
USE some_database;
CREATE TABLE some_Log(datetime DATETIME NOT NULL, temperature FLOAT(5,2) NOT NULL, humidity FLOAT(5,2) NOT NULL, moisture INTEGER NOT NULL);
DESCRIBE some_Log;
```
Your MySQL database should matchup with what you see on phpmyadmin.

**##Step 3: 3rd Party Library Installation**

The Adafruit library is responsible for the DHT_22 functioning properly.
Without installing this library you cannot use the DHT_22 sensor.

It's recommended to clone to your local /var/www/html directory. If you do follow this, then you should delete the original contents that was created when you installed apache by doing-
```
cd /var/www/html/
sudo rm *
```

Now do these steps-

```
git clone https://github.com/N02775223/ELSpring2017
sudo apt-get install build-essential python-dev
cd ELSpring2017
cd Adafruit_Python_DHT
sudo python setup.py install
cd ..
```

**##Step 4: Installing Expect and Bash**

This project uses shell scripts to automate everything. You do not need to run these scripts for the program to work, but it's highly recommended.
```
sudo apt-get install expect
sudo apt-get install bash
chmod a+x Expect.exp
chmod +x Wyvern.sh
chmod +x Wyvern2.sh
```


