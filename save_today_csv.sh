#!/bin/sh

date=$(date +%Y-%m-%d)
mkdir ~/Youbike2.0/$date
for file in $(ls /home/student/07/b07902027/Youbike2.0/station_data)
do
	mv /home/student/07/b07902027/Youbike2.0/station_data/${file} /home/student/07/b07902027/Youbike2.0/$date/
done
