#!/bin/bash
ssh XXXXXXX@wyvern.cs.newpaltz.edu 'mysql -h wyvern -p[PASSWORD] [DATABASE] -e "SOURCE /home/XXXXXX/WWW/Log.sql"'
