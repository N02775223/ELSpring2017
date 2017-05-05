#!/bin/bash
mysqldump -u [USER] -p[PASSWORD] --skip-opt --add-drop-table --skip-extended-insert --skip-add-locks [DATABASE]  > Log.sql


