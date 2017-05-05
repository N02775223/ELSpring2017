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

**##Step 3: Cloning From Github and Installing Libraries**

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
The only files/folders from ELSpring2017 that you really need in '/var/www/html/' are bootstrap, css, img, js, node_modules, browserconfig.xml, and index.php. Later on we'll get into setting up the scripts, but keep in mind that these scripts can be run from any directory.


**##Step 4: Installing Expect and Bash**

This project uses shell scripts to automate updating the remote webserver.
```
sudo apt-get install expect
sudo apt-get install bash
chmod a+x Expect.exp
chmod +x Wyvern.sh
chmod +x Wyvern2.sh
```

**##Step 5: Editing the Scripts**

You will need to insert your information into the following scripts-
```
ELProject.py
Expect.exp -Enter information related to your New Paltz account
Run.sh -Enter information related to your local MySQL database
Wyvern.sh -/home/New Paltz Account/WWW <<< "put /home/pi/Local Directory/Log.sql"
Wyvern2.sh -Enter information related to your remote MySQL database
Once enter in all the required information type in-
./Expect.exp
```
The script should now be running and inserting the MySQL database to your remote webserver
WARNING: Sometimes these scripts will crash and possibly reveal the password that you entered. Please use extreme caution when using these scripts in a public setting.

